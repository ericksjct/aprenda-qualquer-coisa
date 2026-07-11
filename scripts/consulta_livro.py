#!/usr/bin/env python3
"""Indice semantico + consulta do livro-base (Fase 07.1, Fatias 2/4 -- G3-G7).

Constroi e consulta um indice hibrido (denso bge-m3 + BM25/FTS5) sobre os
`livro/*.md` page-anchored gerados pelo converte_livro_vlm.py. Cada resultado
devolve trecho + secao + PAGINA + caminho da imagem da pagina (rede de
seguranca de fidelidade, G2). Roda local, sem tokens; requer o venv de
requirements-ocr.txt (a 1a indexacao baixa o modelo de embedding ~2GB).

Uso:
    python scripts/consulta_livro.py --slug <slug> --build
    python scripts/consulta_livro.py "<consulta>" --slug <slug> [-k N]

O indice mora em .projetos/<slug>/livro/.index/livro.db (1 arquivo, zero-infra).
"""

import argparse
import re
import sqlite3
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from converte_livro import sanitize_slug  # noqa: E402

EMB_MODEL = "BAAI/bge-m3"
EMB_DIM = 1024
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

_PAGE_RE = re.compile(r"<!-- page: (\d+) -->")


def parse_livro_md(text: str, fname: str) -> list:
    """`livro/*.md` -> secoes {file, section, page, text} (puro, testavel).

    Secao = bloco sob um `## `; a pagina e a da ultima ancora vista antes do
    inicio da secao (a ancora e por pagina, a secao herda a corrente).
    """
    sections = []
    current = {"file": fname, "section": "", "page": None, "lines": []}
    page = None
    for line in text.splitlines():
        m = _PAGE_RE.match(line.strip())
        if m:
            page = int(m.group(1))
            continue
        if line.startswith("## ") or line.startswith("# "):
            if current["lines"]:
                sections.append(current)
            current = {
                "file": fname,
                "section": line.lstrip("# ").strip(),
                "page": page,
                "lines": [],
            }
            continue
        if line.strip():
            if current["page"] is None:
                current["page"] = page
            current["lines"].append(line)
    if current["lines"]:
        sections.append(current)
    for s in sections:
        s["text"] = "\n".join(s.pop("lines"))
    return sections


def chunk_sections(sections: list, size: int = CHUNK_SIZE,
                   overlap: int = CHUNK_OVERLAP) -> list:
    """Secao -> chunks de ~size chars com overlap; parent = secao inteira (G6)."""
    chunks = []
    for s in sections:
        text = s["text"]
        start = 0
        while start < len(text):
            piece = text[start:start + size]
            chunks.append({
                "file": s["file"], "section": s["section"],
                "page": s["page"], "text": piece, "parent": text,
            })
            if start + size >= len(text):
                break
            start += size - overlap
    return chunks


def _fts_query(q: str) -> str:
    terms = re.findall(r"\w+", q, re.UNICODE)
    return " OR ".join(f'"{t}"' for t in terms) or '""'


def _serialize(vec) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def _open_db(index_dir: Path) -> sqlite3.Connection:
    import sqlite_vec

    db = sqlite3.connect(index_dir / "livro.db")
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)
    return db


def _embedder():
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(EMB_MODEL)


def build(livro_dir: Path) -> None:
    files = sorted(p for p in livro_dir.glob("*.md"))
    if not files:
        sys.exit(f"nenhum .md em {livro_dir}; rode o converte_livro_vlm.py antes")

    chunks = []
    for f in files:
        sections = parse_livro_md(f.read_text(encoding="utf-8"), f.name)
        chunks.extend(chunk_sections(sections))
    print(f"[*] {len(files)} arquivos -> {len(chunks)} chunks")

    index_dir = livro_dir / ".index"
    index_dir.mkdir(exist_ok=True)
    (index_dir / "livro.db").unlink(missing_ok=True)
    db = _open_db(index_dir)
    db.execute("CREATE TABLE chunk(id INTEGER PRIMARY KEY, file TEXT, "
               "section TEXT, page INTEGER, text TEXT, parent TEXT)")
    db.execute("CREATE VIRTUAL TABLE chunk_fts USING fts5(text)")
    db.execute(f"CREATE VIRTUAL TABLE chunk_vec USING vec0(embedding float[{EMB_DIM}])")

    print(f"[*] carregando {EMB_MODEL} (1a vez baixa ~2GB)...")
    model = _embedder()
    embs = model.encode([c["text"] for c in chunks], normalize_embeddings=True,
                        show_progress_bar=True, batch_size=32)
    for i, (c, e) in enumerate(zip(chunks, embs), 1):
        db.execute("INSERT INTO chunk VALUES (?, ?, ?, ?, ?, ?)",
                   (i, c["file"], c["section"], c["page"], c["text"], c["parent"]))
        db.execute("INSERT INTO chunk_fts(rowid, text) VALUES (?, ?)", (i, c["text"]))
        db.execute("INSERT INTO chunk_vec(rowid, embedding) VALUES (?, ?)",
                   (i, _serialize(e.tolist())))
    db.commit()
    db.close()
    print(f"OK: indice em {index_dir / 'livro.db'}")


def query(livro_dir: Path, q: str, k: int) -> list:
    db = _open_db(livro_dir / ".index")
    emb = _embedder().encode([q], normalize_embeddings=True)[0]

    dense = db.execute(
        "SELECT rowid FROM chunk_vec WHERE embedding MATCH ? "
        "ORDER BY distance LIMIT ?", (_serialize(emb.tolist()), k * 4)
    ).fetchall()
    try:
        sparse = db.execute(
            "SELECT rowid FROM chunk_fts WHERE chunk_fts MATCH ? "
            "ORDER BY bm25(chunk_fts) LIMIT ?", (_fts_query(q), k * 4)
        ).fetchall()
    except sqlite3.OperationalError:
        sparse = []

    # fusao por rank reciproco (RRF): robusta sem tuning de pesos
    score: dict = {}
    for rank, (rid,) in enumerate(dense):
        score[rid] = score.get(rid, 0) + 1 / (60 + rank)
    for rank, (rid,) in enumerate(sparse):
        score[rid] = score.get(rid, 0) + 1 / (60 + rank)
    top = sorted(score, key=score.get, reverse=True)[:k]

    results = []
    for rid in top:
        row = db.execute("SELECT file, section, page, text FROM chunk "
                         "WHERE id = ?", (rid,)).fetchone()
        results.append(row)
    db.close()
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("consulta", nargs="?", default=None)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--build", action="store_true", help="(re)constroi o indice")
    parser.add_argument("-k", type=int, default=3, help="resultados (default: 3)")
    args = parser.parse_args()

    slug = sanitize_slug(args.slug)
    livro_dir = Path(".projetos") / slug / "livro"
    if not livro_dir.is_dir():
        sys.exit(f"nao existe: {livro_dir}")

    if args.build:
        build(livro_dir)
        return
    if not args.consulta:
        sys.exit("informe uma consulta ou --build")

    for file, section, page, text in query(livro_dir, args.consulta, args.k):
        img = livro_dir / ".paginas" / f"page-{page:04d}.png" if page else None
        print(f"--- pagina {page} | {section} | {file}")
        if img and img.is_file():
            print(f"    imagem: {img}")
        print("    " + " ".join(text.split())[:400])
        print()


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
