# Phase 7: Ingestao de PDF do livro via docling - Pattern Map

**Mapped:** 2026-06-21
**Files analyzed:** 8 (3 NEW code/deps, 1 NEW skill, 3 EDIT mentor docs, 3 NEW test files, + AGENTS.md edit)
**Analogs found:** 5 exact/role-match in-repo + 1 external base script / 8 deliverable groups

> Repo conventions the planner MUST respect (from `mentor/reference.md` and `AGENTS.md`):
>
> - Artefatos sob `.projetos/<slug>/` (saida do livro) = **portugues ACENTUADO**, UTF-8.
> - Docs internos do agente (`mentor/`, `.claude/skills/`, `AGENTS.md`, `.planning/`) = **ASCII puro, sem acento**.
> - Todo `.md` gerado obedece markdownlint (MD022/MD031/MD032/MD040/MD025/MD012/MD009/MD047).
> - Fonte-unica: a logica do metodo vive em `mentor/<comando>.md`; skills e AGENTS.md so APONTAM, nunca duplicam.
> - Core do toolkit e stdlib-only; dep nova (`docling`) e opt-in e isolada.

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `scripts/converte_livro.py` (NEW) | utility CLI | file-I/O + transform (PDF -> md) | `scripts/roadmap_fetch.py` (CLI style) + EXTERNAL `converter.py` (conversion engine) | role-match (style) + exact (engine) |
| `requirements-pdf.txt` (NEW) | config / deps manifest | n/a | none in-repo (stdlib-only repo) | NO ANALOG |
| `.claude/skills/converte-livro/SKILL.md` (NEW) | skill adapter | request-response (agent -> mentor doc) | `.claude/skills/tutor/SKILL.md`, `novo-projeto/SKILL.md`, `fecha-marco/SKILL.md` | exact |
| `mentor/novo-projeto.md` (EDIT) | method doc (procedure) | event-driven (bootstrap step) | its own Passo 3 (roadmap_fetch integration) | exact (self) |
| `mentor/tutor.md` (EDIT) | method doc (procedure) | request-response (consult livro/ + page ref) | its own Passo 0 (read `.projetos/<slug>/` artifacts) + Passo 3 | exact (self) |
| `mentor/reference.md` (EDIT) | method doc (layout + templates) | reference/transform | its own layout block + "Idioma e acentuacao" section + APRENDIZADO template | exact (self) |
| `AGENTS.md` (EDIT) | config / tool registry | request-response | its `## Ferramentas` + `## Nota por ferramenta` blocks | exact (self) |
| `tests/test_converte_livro.py` (NEW) | test | unit (synthetic DoclingDocument) | none in-repo (no pytest yet) | NO ANALOG |
| `tests/conftest.py` (NEW) | test fixture | n/a | none in-repo | NO ANALOG |
| `tests/fixtures/sample.pdf` (NEW) | test fixture (binary) | n/a | none in-repo | NO ANALOG |

## Pattern Assignments

### `scripts/converte_livro.py` (utility CLI, file-I/O + transform)

Two analogs combine: the **CLI shell/style** comes from `scripts/roadmap_fetch.py` (in-repo), and the **conversion engine** comes from the EXTERNAL base script `C:\Users\Erick\Documents\Projetos\docling-extrair-pdf\converter.py`. The planner adapts the engine into the roadmap_fetch CLI skin.

**Analog A (CLI style):** `scripts/roadmap_fetch.py`

Module docstring + usage block (lines 1-16) — copy this shape (one-line summary, then `Uso:` examples), `argparse` driven:

```python
"""Baixa um roadmap do roadmap.sh e gera uma referencia markdown ordenada.
...
Uso:
    python scripts/roadmap_fetch.py frontend
    python scripts/roadmap_fetch.py python -o referencias/
"""
import argparse
import sys
from pathlib import Path
```

`argparse` + output-dir + `.write_text(..., encoding="utf-8")` + terminal `print("OK: ...")` pattern (lines 142-168) — the converte_livro CLI mirrors this exactly: positional `<pdf>`, `--slug`, optional `--out`/`--cut-level`, write under `.projetos/<slug>/livro/`, print an `OK:` summary line at the end:

```python
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("slug", help="slug do roadmap (ex: frontend, python, backend)")
    parser.add_argument("-o", "--out-dir", default="referencias", ...)
    args = parser.parse_args()
    ...
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"roadmap-{args.slug}.md"
    out_path.write_text(render_markdown(...), encoding="utf-8")
    print(f"OK: {out_path} ({len(outline)} topicos, {n_subs} subtopicos)")

if __name__ == "__main__":
    main()
```

Note: `roadmap_fetch.py` exits with a friendly `sys.exit("...")` on bad input (lines 36-40, 156) — reuse for `--slug` validation (ASVS V5: reject `..` / path separators, whitelist `[a-z0-9-]` per `mentor/novo-projeto.md:107` slug convention) and "PDF nao existe".

**Analog B (conversion engine):** EXTERNAL `C:\Users\Erick\Documents\Projetos\docling-extrair-pdf\converter.py`

PRESERVE verbatim — memory-hardening env guards, set BEFORE importing docling (lines 8-16):

```python
# --- BLINDAGEM DE MEMORIA (C++) --- evita std::bad_alloc limitando threads do OCR
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
# docling imports come AFTER the env guards
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
```

PRESERVE — pipeline options (`do_ocr`, `generate_picture_images`) (lines 54-62). RESEARCH adds `AcceleratorOptions(num_threads=1, device=CPU)` (see RESEARCH Pattern 1) and converts the WHOLE pdf in one `convert()` call instead of the per-page pypdf loop:

```python
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = True
pipeline_options.generate_picture_images = True
converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)
```

PRESERVE verbatim — final markdownlint `--fix` pass with graceful `FileNotFoundError` (lines 108-126), `shell=True` for Windows:

```python
try:
    resultado_lint = subprocess.run(
        ["markdownlint", "--fix", str(md_output_path)],
        capture_output=True, text=True, check=False,
        shell=True,  # Windows
    )
except FileNotFoundError:
    print("    [!] Aviso: 'markdownlint' nao encontrado no sistema.")
    print("    Certifique-se de rodar: npm install -g markdownlint-cli")
```

PRESERVE — page-progress print (line 78), exposed for D-14 ("pagina N de M"):

```python
print(f"    -> Processando pagina {num_pagina_atual} de {total_paginas}...", end=" ", flush=True)
```

**REMOVE from base script (per D-12 / RESEARCH):**

- `questionary.select` interactive picker (lines 6, 37-44) -> replaced by `argparse` positional `<pdf>`.
- `pdfs/` + `output/` hardcoded dirs (lines 22-49) -> write under `.projetos/<slug>/livro/`.
- The pypdf 1-page chunk loop as PRIMARY path (lines 65-105) — RESEARCH Anti-Pattern: it destroys D-09 (cross-page headings) and D-10 (`page_no` always 1). Keep `pypdf` only as an OOM `page_range` batch fallback.
- The `---` separator (line 96) -> replaced by `<!-- page: N -->` anchor from `item.prov[0].page_no` (D-10, RESEARCH Pattern 3).

**NEW logic (no analog — from RESEARCH, the testable core):** deterministic chapter split via `doc.iterate_items()` on `TITLE`/`SECTION_HEADER<=cut_level` (RESEARCH Pattern 2) and `_page_of(item)` anchor helper (RESEARCH Pattern 3). These functions must be importable/pure so `tests/test_converte_livro.py` can drive them with a synthetic document.

> **Accent rule (CRITICAL):** the book markdown written into `livro/` is a STUDENT artifact -> preserve the source language / accented Portuguese (`mentor/reference.md:30-35`). Do NOT route book text through ASCII normalization. The script's own console prints and code comments stay ASCII (internal-facing), but file CONTENT it writes is verbatim docling output.

---

### `requirements-pdf.txt` (config / deps manifest) — NO IN-REPO ANALOG

The repo is stdlib-only; there is no existing requirements/pyproject file to copy. Introduce as a standalone opt-in file at repo root (per RESEARCH "Recommended Project Structure"), NEVER folded into a global/shared requirements (would break D-05/D-07 isolation). Suggested content (RESEARCH Standard Stack, lines 149-152):

```text
docling>=2.104.0
pypdf>=4.0
```

Install path is documented (not auto-run) — venv + pip, surfaced by the mentor/skill, not executed silently:

```bash
python -m venv .venv-pdf
.\.venv-pdf\Scripts\activate
pip install -r requirements-pdf.txt
```

`pytest` for tests goes into the SAME opt-in venv (RESEARCH Wave 0), not the core. Planner decides whether to add `pytest` to `requirements-pdf.txt` or a separate `requirements-dev.txt`.

---

### `.claude/skills/converte-livro/SKILL.md` (skill adapter, request-response)

**Analog:** `.claude/skills/tutor/SKILL.md` (and identical shape in `novo-projeto`, `fecha-marco`, `debug`, `spidr-split`).

Every existing skill is a thin adapter: YAML frontmatter (`name` + `description`) then a 2-3 line body that POINTS to the canonical `mentor/<comando>.md` and restates the `/comando` convention. Do NOT duplicate method logic here. Exact template to copy (`tutor/SKILL.md` lines 1-13):

```markdown
---
name: tutor
description: Sessao de tutoria copiloto. Use quando o aluno... [trigger phrases]
---

# Tutor Copiloto (adaptador Claude Code)

Leia `mentor/tutor.md` na raiz deste repositorio e siga o procedimento exatamente,
comecando pelo Passo 0 (restaurar contexto).

Convencao: quando o documento citar um `/comando`, e a skill correspondente
(conteudo canonico em `mentor/<comando>.md`).
```

For `converte-livro`, the body points at the canonical conversion procedure. NUANCE per D-15: the method logic ("tem livro-base? PDF ou .md", surface the exact command, D-14 pre-warning) lives in `mentor/novo-projeto.md` (single source). The skill body must reference that — it does NOT re-explain docling. The `description` is the trigger surface; write it ASCII, no accents. Per D-14, the procedure the skill points to must pre-warn: "vai demorar, nao consome tokens (roda local), mostra progresso pagina N de M".

---

### `mentor/novo-projeto.md` (EDIT — method doc) — D-02, D-15

**Analog:** its own **Passo 3 — Referencia externa (recomendado)** (lines 34-50), which is the structural twin of the new book-bootstrap step: an optional tool step that surfaces an exact command and writes under `.projetos/<slug>/`.

Passo 3 anatomy to mirror, in order: a `## Passo N` heading -> optional framing sentence ("Se a stack corresponde...") -> a fenced `text` block with the EXACT command (`python scripts/roadmap_fetch.py <slug> -o .projetos/<slug>/referencias/`) -> bullet rationale ("a saida deve ficar DENTRO da pasta do projeto do aluno") -> a graceful-skip closing bullet ("Se o script nao estiver acessivel ... siga sem ele"). The new book-bootstrap step reuses this exact skeleton, swapping in the `converte_livro.py` venv command and the D-15 PDF-vs-`.md` branch.

The new step (livro-base, near Passo 3) is OPTIONAL and follows the same anatomy. D-15 content the planner weaves: mentor PERGUNTA "tem livro-base? (PDF ou .md)"; if `.md` -> instruct paste into `livro/` (zero deps, D-06); if PDF -> surface the EXACT venv-prefixed command (Pitfall 3) OR fire the `/converte-livro` skill, with the D-14 pre-warning, then proceed once `livro/` is populated. "O mentor nunca roda docling silenciosamente; so consome o resultado." Also reference `livro/` in Passo 7 esqueleto list (lines 104-116), alongside `referencias/`.

> ASCII (internal doc). The fenced command must show explicit venv activation (Pitfall 3) and require Python 3.10+.

---

### `mentor/tutor.md` (EDIT — method doc) — D-10, D-01

**Analog:** its own **Passo 0** (lines 12-33, reading `.projetos/<slug>/` artifacts in order) and **Passo 3 — Conduzir o passo atual** (lines 66-81).

Passo 0 already enumerates the ordered reads (`PROGRESSO.md`, `CAMINHO.md`, `aulas/...`, `APRENDIZADO.md`). The edit adds `livro/*.md` as a baseline source the mentor consults (D-01) when it exists — mirror the existing bulleted read-list style:

```markdown
- `PROGRESSO.md` — marco atual, tabela de substrato, dividas abertas, ultimo log.
- `CAMINHO.md` — os passos (P0x) do marco atual: conceito, pressupostos, entregavel.
- `aulas/P0x-<slug>.md` do passo atual — a teoria minima do passo de hoje...
```

Passo 3 step 1 ("Conceito em dois canais") is where the page-reference (D-10) is woven: when consulting the book, the tutor can cite "ve a pagina X do livro" using the `<!-- page: N -->` anchor the script wrote. Add as a refinement to the existing "intuicao -> exemplo -> conceito formal -> aplicacao" flow, not a new top-level step.

D-03/D-04 divergence protocol (mentor decides alone; logs to APRENDIZADO.md) is referenced here and detailed in `reference.md`. NEVER ship D-03 without D-04 (CONTEXT nuance). The forense Passo 6 in `reference.md:477-486` already writes to APRENDIZADO.md — the divergence log reuses that artifact, not a new one.

> ASCII (internal doc).

---

### `mentor/reference.md` (EDIT — method doc / layout + templates) — D-08, D-04

**Analog:** its own **Layout do repo do aluno** block (lines 221-238) and **Template — APRENDIZADO.md** (lines 298-318), plus the existing **Idioma e acentuacao** section (lines 22-43) which already covers the accent rule for student artifacts.

Add `livro/` to the layout tree (mirror the existing comment style; place it as a NEW sibling of `referencias/`, distinct from it — D-08 separates book-base from roadmap output):

```text
.projetos/<slug>/
|-- ...
|-- referencias/          # roadmaps de referencia (scripts/roadmap_fetch.py)
|-- livro/                # NEW: markdown do livro-base do aluno (docling OU colado)
|   `-- 0x-<capitulo>.md   #   um arquivo por capitulo, com <!-- page: N --> anchors
|-- aulas/                # teoria minima POR PASSO (P0x)...
```

APRENDIZADO.md template already has a **Decisoes arquiteturais** dated-entry section (lines 311-313) — the divergence record (D-04) reuses/extends this pattern (dated entry: livro diz X / pratica diz Y / escolha do mentor). Mirror the existing `- AAAA-MM-DD -- <...>` dated-bullet style:

```markdown
## Decisoes arquiteturais

- AAAA-MM-DD -- <decisao tomada> (contexto: <por que escolhemos isso>)
```

The "Idioma e acentuacao" section (lines 22-43) ALREADY mandates accented Portuguese for student artifacts and lists `livro/`-class files implicitly ("qualquer outro texto que o ALUNO le") — the planner should confirm `livro/` content falls under this rule (it does) and need only reference it, not rewrite it.

> The template TEXT inside `reference.md` is copied into student artifacts -> the fixed Portuguese in those fenced templates is intentionally ACCENTED (reference.md:40-43). The surrounding prose of `reference.md` itself is ASCII.

---

### `AGENTS.md` (EDIT — config / tool registry) — D-13

**Analog:** its own `## Ferramentas` block (lines 50-54, registering `roadmap_fetch.py`) and `## Nota por ferramenta` -> Claude Code bullet (lines 57-60, listing native skills).

Register the new converter the same way `roadmap_fetch.py` is registered, and add `/converte-livro` to the native-skills list. Mirror exactly:

```markdown
## Ferramentas

- `python scripts/roadmap_fetch.py <slug> -o .projetos/<slug>/referencias/` — baixa um
  roadmap do roadmap.sh ... Usado no bootstrap (`mentor/novo-projeto.md`, Passo 3).
```

```markdown
- **Claude Code**: as skills nativas (`/novo-projeto`, `/tutor`, `/fecha-marco`,
  `/debug`, `/spidr-split`) ... apontam para `mentor/` — use-os.
```

Add `/converte-livro` to that skill list and a `Ferramentas` bullet for `scripts/converte_livro.py` (note the opt-in venv / `requirements-pdf.txt`, and that it is OPTIONAL — core stays stdlib).

> ASCII (internal doc).

---

### `tests/test_converte_livro.py`, `tests/conftest.py`, `tests/fixtures/sample.pdf` (NEW) — NO IN-REPO ANALOG

There is **no pytest, no `tests/`, no `conftest.py`, no `pyproject.toml`** anywhere in the repo (verified via glob — zero matches). This is the Wave 0 framework-introduction gap (RESEARCH "Wave 0 Gaps", lines 483-491). The planner has no in-repo test to copy from; use RESEARCH's "Phase Requirements -> Test Map" (lines 465-475) as the spec.

Structure to build (from RESEARCH Validation Architecture):

- `tests/conftest.py` — fixture that builds a SYNTHETIC `DoclingDocument` in memory (minimal items with `label`/`level`/`prov[0].page_no`) so split/anchor logic is tested WITHOUT running the heavy docling pipeline; plus a `@pytest.mark.slow` skip-if-docling-missing marker.
- `tests/test_converte_livro.py` — unit tests mapping 1:1 to D-NN: `test_split_by_heading`, `test_chapter_count` (D-09), `test_page_anchor_present`, `test_page_anchor_value` (D-10), `test_env_guards`, `test_lint_called` (subprocess mocked, D-12), `test_accents_preserved` (D-15, asserts NO ASCII normalization of book text).
- `tests/fixtures/sample.pdf` — tiny 2-3 page PDF with 2 headings for the `@pytest.mark.slow` golden-file smoke.

For tests to be writable, `converte_livro.py` must expose the split and `_page_of` helpers as importable pure functions (the synthetic-document approach depends on it). This couples the test design to the script design — plan them in the same wave.

> Tests live with the opt-in script and stay OUT of the core's "zero setup" promise (RESEARCH Wave 0). `pytest` installs into the PDF venv only.

## Shared Patterns

### Single-source method (adapters point, never duplicate)

**Source:** all `.claude/skills/*/SKILL.md` (e.g. `tutor/SKILL.md:8-13`) + `AGENTS.md:57-60`
**Apply to:** `.claude/skills/converte-livro/SKILL.md`, `AGENTS.md` edit

```markdown
Leia `mentor/<comando>.md` na raiz deste repositorio e siga o procedimento exatamente.

Convencao: quando o documento citar um `/comando`, e a skill correspondente
(conteudo canonico em `mentor/<comando>.md`).
```

The D-15 book-bootstrap logic, D-14 pre-warning, and D-03/D-04 divergence protocol are method content -> they live in `mentor/*.md`. Skills/AGENTS.md only point.

### Idioma e acentuacao (two audiences)

**Source:** `mentor/reference.md:22-43`
**Apply to:** every file in this phase

- Student-facing (`.projetos/<slug>/livro/**`, the converted book) -> ACCENTED Portuguese / source language, UTF-8. NEVER ASCII-normalize book text (RESEARCH Anti-Pattern).
- Internal (`scripts/*.py` comments+prints, `mentor/*.md`, `.claude/skills/**`, `AGENTS.md`, `tests/**`) -> ASCII, no accents.

### markdownlint on generated markdown

**Source:** `mentor/reference.md:3-18`; enforced in the script via `markdownlint --fix` (base `converter.py:108-126`)
**Apply to:** the converted `livro/*.md` (script runs `--fix`) AND every `.md` the planner/persona writes (MD022/MD031/MD032/MD040/MD025/MD012/MD009/MD047).

### Opt-in / isolated dependency (core stays stdlib)

**Source:** `scripts/roadmap_fetch.py` (stdlib-only precedent: `argparse`, `urllib`, `pathlib`, `json` only — no third-party imports)
**Apply to:** `converte_livro.py` + `requirements-pdf.txt`

The new docling dep is isolated in one script + one requirements file + a dedicated venv. `roadmap_fetch.py` and the core are untouched. D-06: `.md`-already path needs zero deps.

### Slug path-safety (ASVS V5)

**Source:** slug convention `mentor/novo-projeto.md:107` (kebab-case) + `roadmap_fetch.py` friendly `sys.exit` on bad input
**Apply to:** `converte_livro.py --slug` validation — reject `..`/separators, whitelist `[a-z0-9-]` before writing under `.projetos/<slug>/livro/` (RESEARCH Security Domain).

## No Analog Found

| File | Role | Data Flow | Reason / Where to source pattern instead |
|------|------|-----------|------------------------------------------|
| `requirements-pdf.txt` | config/deps | n/a | Repo is stdlib-only; no requirements file exists. Use RESEARCH Standard Stack (lines 138-157). Standalone, never merged into core. |
| `tests/test_converte_livro.py` | test | unit | No pytest/tests in repo (Wave 0 introduces it). Use RESEARCH Test Map (lines 465-475). |
| `tests/conftest.py` | test fixture | n/a | No conftest exists. Build synthetic `DoclingDocument` per RESEARCH Validation Architecture. |
| `tests/fixtures/sample.pdf` | binary fixture | n/a | No fixtures dir. Tiny 2-3 page, 2-heading PDF for the slow golden smoke. |
| docling split/anchor core logic in `converte_livro.py` | utility | transform | No in-repo analog produces structured-model splits. Source: RESEARCH Patterns 1-4 (sourced from docling-core). |

## Metadata

**Analog search scope:** `scripts/`, `.claude/skills/`, `mentor/`, `AGENTS.md`, repo root (requirements/pyproject/tests glob), + EXTERNAL `C:\Users\Erick\Documents\Projetos\docling-extrair-pdf\converter.py`.
**Files scanned:** `roadmap_fetch.py`, `converter.py` (external), 5 existing `SKILL.md`, `novo-projeto.md`, `tutor.md`, `reference.md`, `AGENTS.md`; glob confirmed 0 requirements/test/pyproject files.
**Pattern extraction date:** 2026-06-21
