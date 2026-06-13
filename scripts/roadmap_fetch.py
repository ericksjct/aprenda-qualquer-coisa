#!/usr/bin/env python3
"""Baixa um roadmap do roadmap.sh e gera uma referencia markdown ordenada.

O roadmap.sh expoe cada roadmap como JSON publico em https://roadmap.sh/<slug>.json
(formato reactflow: nodes + edges). Este script extrai os topicos na ordem visual
de leitura (top-down, que e a ordem canonica do site) com seus subtopicos, e salva
um markdown enxuto que serve de base de ordenacao de conceitos para o /novo-projeto.

Uso:
    python scripts/roadmap_fetch.py frontend
    python scripts/roadmap_fetch.py python -o referencias/

Slugs comuns: frontend, backend, full-stack, python, javascript, typescript,
react, nodejs, sql, devops, android, ai-engineer, data-analyst, golang, java.
Lista completa: https://roadmap.sh/roadmaps
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

BASE_URL = "https://roadmap.sh/{slug}.json"


def fetch_roadmap(slug: str) -> dict:
    url = BASE_URL.format(slug=slug)
    req = urllib.request.Request(url, headers={"User-Agent": "roadmap-fetch/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            sys.exit(
                f"Roadmap '{slug}' nao encontrado (404). "
                "Confira o slug em https://roadmap.sh/roadmaps"
            )
        raise


def build_outline(data: dict) -> list[dict]:
    """Retorna topicos em ordem de leitura, cada um com seus subtopicos."""
    nodes = {n["id"]: n for n in data.get("nodes", [])}
    topics = [n for n in nodes.values() if n.get("type") == "topic"]
    subtopics = {n["id"]: n for n in nodes.values() if n.get("type") == "subtopic"}

    # Subtopicos ligam ao topico pai por arestas, as vezes em cadeia
    # (topic -> subtopic -> subtopic). BFS nao-direcionada a partir de cada
    # topico, sem atravessar outros topicos, atribui cada subtopico ao
    # topico mais proximo.
    adjacency: dict[str, set[str]] = {}
    for edge in data.get("edges", []):
        src, tgt = edge.get("source"), edge.get("target")
        if src in nodes and tgt in nodes:
            adjacency.setdefault(src, set()).add(tgt)
            adjacency.setdefault(tgt, set()).add(src)

    children: dict[str, list[dict]] = {t["id"]: [] for t in topics}
    claimed: set[str] = set()
    for topic in topics:
        queue = [topic["id"]]
        seen = {topic["id"]}
        while queue:
            current = queue.pop(0)
            for neighbor in adjacency.get(current, ()):
                if neighbor in seen or neighbor not in subtopics or neighbor in claimed:
                    continue
                seen.add(neighbor)
                claimed.add(neighbor)
                children[topic["id"]].append(subtopics[neighbor])
                queue.append(neighbor)

    def pos_key(n: dict) -> tuple[float, float]:
        p = n.get("position") or {}
        return (p.get("y", 0.0), p.get("x", 0.0))

    # Fallback: subtopicos sem aresta alguma ficam posicionados visualmente
    # ao lado do topico pai. Atribui cada orfao ao topico mais proximo.
    def center(n: dict) -> tuple[float, float]:
        p = n.get("position") or {}
        return (p.get("x", 0.0), p.get("y", 0.0))

    for sub_id, sub in subtopics.items():
        if sub_id in claimed or not topics:
            continue
        sx, sy = center(sub)
        nearest = min(
            topics,
            key=lambda t: (center(t)[0] - sx) ** 2 + (center(t)[1] - sy) ** 2,
        )
        children[nearest["id"]].append(sub)
        claimed.add(sub_id)

    outline = []
    for topic in sorted(topics, key=pos_key):
        label = (topic.get("data") or {}).get("label", "").strip()
        if not label:
            continue
        subs = sorted(children.get(topic["id"], []), key=pos_key)
        outline.append(
            {
                "label": label,
                "subtopics": [
                    s["data"]["label"].strip()
                    for s in subs
                    if (s.get("data") or {}).get("label", "").strip()
                ],
            }
        )
    return outline


def render_markdown(slug: str, data: dict, outline: list[dict]) -> str:
    title = data.get("title") or slug
    if isinstance(title, dict):
        # Alguns roadmaps usam {'card': ..., 'page': ...} como titulo.
        title = title.get("page") or title.get("card") or slug
    desc = (data.get("description") or "").strip()
    lines = [
        f"# Roadmap de referencia — {title}",
        "",
        f"> Fonte: https://roadmap.sh/{slug} (gerado por scripts/roadmap_fetch.py).",
        "> Ordem dos topicos = ordem canonica de leitura do roadmap original.",
        "> Use como base de ORDENACAO DE CONCEITOS, nao como curriculo a copiar:",
        "> o caminho do aluno deve continuar sendo fatiado em marcos verticais.",
        "",
    ]
    if desc:
        lines += [desc, ""]
    for i, topic in enumerate(outline, 1):
        lines.append(f"## {i:02d}. {topic['label']}")
        lines.append("")
        for sub in topic["subtopics"]:
            lines.append(f"- {sub}")
        if topic["subtopics"]:
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("slug", help="slug do roadmap (ex: frontend, python, backend)")
    parser.add_argument(
        "-o",
        "--out-dir",
        default="referencias",
        help="diretorio de saida (default: referencias/)",
    )
    args = parser.parse_args()

    data = fetch_roadmap(args.slug)
    outline = build_outline(data)
    if not outline:
        sys.exit(f"Roadmap '{args.slug}' baixado, mas sem topicos extraiveis.")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"roadmap-{args.slug}.md"
    out_path.write_text(render_markdown(args.slug, data, outline), encoding="utf-8")

    n_subs = sum(len(t["subtopics"]) for t in outline)
    print(f"OK: {out_path} ({len(outline)} topicos, {n_subs} subtopicos)")


if __name__ == "__main__":
    main()
