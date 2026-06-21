# Phase 7: Ingestao de PDF do livro via docling - Research

**Researched:** 2026-06-21
**Domain:** PDF -> structured markdown via `docling` (deterministic chapter split + page anchors), as an OPT-IN Python CLI woven into a stdlib-only markdown method toolkit
**Confidence:** HIGH (docling API verified via Context7/docling-core source + PyPI; toolkit conventions verified in-repo)

## Summary

The phase adds the first executable third-party dependency to a toolkit that is otherwise
100% markdown + one stdlib Python utility. The deliverable is a CLI converter adapted from an
existing working script (`converter.py`) that turns a student's book PDF into structured
markdown under `.projetos/<slug>/livro/`, with deterministic chapter/section split (D-09) and
per-chunk page anchors (D-10), plus the method weaving in `mentor/*.md`.

The central technical finding reshapes the base script's approach: **docling's `convert()`
natively accepts `page_range=(start, end)` and exposes a full structured document model
(`DoclingDocument`) where every element carries `prov[0].page_no` and section headers carry a
`level` integer.** This means the deterministic split (D-09) and page anchors (D-10) should be
driven from docling's structured model — NOT by post-processing concatenated per-page markdown.
The base script's pypdf 1-page-chunking pattern actively destroys both signals (a heading
spanning a page boundary is lost; `page_no` is always 1 inside a 1-page chunk). docling also
exposes `export_to_markdown(..., page_no=N, from_element, to_element, labels, page_break_placeholder=...)`,
giving deterministic page-scoped and element-range slicing for free.

**Primary recommendation:** Convert the whole PDF in ONE `convert()` call (preserving structure
and native page provenance), control memory via `AcceleratorOptions(device=CPU, num_threads=1)` +
the existing OMP/MKL env guards (and `page_range` batching ONLY as a fallback for OOM on huge
books), then split deterministically by iterating `doc.iterate_items()` on `SECTION_HEADER`/`TITLE`
boundaries, emitting one `.md` per chapter into `livro/` with a `<!-- page: N -->` anchor sourced
from each item's `prov[0].page_no`. Preserve the memory-hardening env vars and the final
`markdownlint --fix` step verbatim. Keep `docling`+`pypdf` in a dedicated `requirements-pdf.txt`
installed into a project-local venv; the toolkit core stays stdlib-only and untouched.

## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01:** O livro convertido serve como **guideline/baseline teorico** do mentor — literatura-base
  que o mentor respeita, nao so combustivel de ordenacao.
- **D-02:** Entra como **passo opcional no bootstrap** (`mentor/novo-projeto.md`), proximo do Passo 3.
  Fonte-unica: logica vive em `mentor/`, nunca duplicada nos adaptadores.
- **D-03:** **Protocolo de divergencia** — quando a pesquisa do mentor diverge do livro, o **mentor
  decide sozinho** (criterio proprio, ex.: recencia/consenso). Nao pergunta ao aluno por caso.
- **D-04:** Cada divergencia vira **entrada datada em `.projetos/<slug>/APRENDIZADO.md`** (livro diz X
  x pratica diz Y x escolha do mentor). Costurar D-03/D-04 SEMPRE juntos.
- **D-05:** `docling` e dependencia **OPCIONAL**, isolada nesse script. Core 100% stdlib-only e
  intocado (como `roadmap_fetch.py`). Contrato do metodo = markdown em `livro/`, nao docling.
- **D-06:** Quem ja tem o livro em `.md` apenas **cola o arquivo em `livro/`** — sem dependencia nova.
- **D-07:** Isolar a dep via **`requirements` opcional + venv** (ex.: `requirements-pdf.txt`). Explicito
  que e opt-in. Deps base: `docling`, `pypdf`, `questionary` (REMOVER — D-12), + `markdownlint-cli` (npm).
- **D-08:** Markdown do livro mora em **`.projetos/<slug>/livro/`** (pasta NOVA no layout). Separa a
  fonte-base de `referencias/` (saida do roadmap.sh).
- **D-09:** **Split por capitulo/secao** seguindo headings que o docling detecta — por **script
  deterministico**, nao pela LLM. Principio: maximizar trabalho deterministico.
- **D-10:** **Ancora de pagina deterministica** em cada trecho (ex.: `<!-- page: N -->`) pra o tutor
  citar a pagina exata. Formato exato e detalhe de planejamento.
- **D-11:** Fidelidade: **estrutura (headings/secoes/ordem) > tabelas/figuras/formulas**.
  Tabelas/formulas/figuras sao best-effort; nao travam a phase.
- **D-12:** **Adaptar `converter.py`**: remover `questionary.select`, virar **CLI por args** (ex.:
  `python scripts/<script>.py <pdf> --slug <slug>`), gravar em `.projetos/<slug>/livro/`. Preservar
  blindagem de memoria (threads=1 + chunking) e `markdownlint --fix`.
- **D-13:** **Dois caminhos**: (a) aluno roda no terminal; (b) agente dispara via **skill** (ex.:
  `/converte-livro`) ou passo do bootstrap.
- **D-14:** Quando o agente dispara, ele **avisa ANTES**: vai **demorar**, **nao consome tokens**
  (roda local), **mostra progresso** ("pagina N de M").
- **D-15:** No bootstrap o mentor **pergunta**: "tem livro-base? (PDF ou `.md`)". Se `.md`: cola em
  `livro/`. Se PDF: mostra a linha de comando exata (ou skill). **O mentor nunca roda docling
  silenciosamente; so consome o resultado.**

### Claude's Discretion

- Nome exato da skill e do script; formato exato da ancora de pagina (HTML comment vs heading);
  nome do arquivo de requirements opcional; criterio de corte do split (H1 vs H2); tratamento de
  livro em idioma diferente do repo (preservar idioma da fonte e o esperado).

### Deferred Ideas (OUT OF SCOPE)

- Alta-fidelidade de tabelas/formulas/figuras (best-effort agora — D-11).
- i18n do toolkit (outro item v2.0).
- Atualizar PROJECT.md (mover "codigo de aplicacao/runtime novo" de Out of Scope para Validated na
  transicao de milestone).

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| PDF -> markdown conversion | Python CLI script (`scripts/`) | docling library | Heavy, local, deterministic; never the LLM (D-09, D-14) |
| Chapter/section split | Python CLI script | docling structured model | Deterministic loop over `iterate_items()`; D-09 forbids LLM |
| Page anchors | Python CLI script | docling `prov.page_no` | Page number comes from docling provenance, written by the script (D-10) |
| markdown lint cleanup | `markdownlint-cli` (npm) via subprocess | — | Existing repo convention; runs once at end |
| "tem livro-base?" prompt + command surfacing | Mentor (LLM) reading `mentor/novo-projeto.md` | skill `/converte-livro` | LLM orchestrates, never runs docling silently (D-15) |
| Divergence protocol + dated log | Mentor (LLM) | `APRENDIZADO.md` artifact | Judgment + transparency record (D-03/D-04) |
| Consuming book as baseline during tutoring | Mentor (LLM) reading `livro/*.md` | `mentor/tutor.md` | LLM reads the produced markdown; page anchor enables "ve a pagina X" |

<phase_requirements>
## Phase Requirements

No formal REQUIREMENTS.md exists for this phase. The locked decisions **D-01..D-15 ARE the
requirements** (see User Constraints above). The planner should map each plan task back to the
specific D-NN it satisfies. The research-support mapping:

| D-NN | Research Support |
|------|------------------|
| D-09 (deterministic split) | `doc.iterate_items()` yields `SectionHeaderItem.level` + `DocItemLabel.SECTION_HEADER`/`TITLE` — verified split boundary signal (Code Examples) |
| D-10 (page anchor) | `item.prov[0].page_no` per element; OR `export_to_markdown(page_break_placeholder=...)` — verified (Code Examples) |
| D-12 (adapt + preserve memory/lint) | `AcceleratorOptions(device=CPU, num_threads=1)` + env guards + native `page_range` replace pypdf split; subprocess markdownlint preserved (Patterns) |
| D-05/D-07 (isolated opt-in dep) | `requirements-pdf.txt` + venv; docling pulls torch (~2GB) + HF model download on first run (Environment Availability) |
| D-13/D-14 (skill + pre-warn) | docling's own agent-skill example confirms agent-driven, deterministic, script-prescribed flow (State of the Art) |
</phase_requirements>

## Standard Stack

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| `docling` | 2.104.0 (latest); 2.81.0 already installed on this machine | PDF -> `DoclingDocument` -> markdown, with layout/OCR/structure | The library the base script already uses; provides structured model + native page provenance [VERIFIED: PyPI `pip index versions docling`] |
| `pypdf` | latest (2.x) | (Fallback only) split PDF into page-range batches if a single `convert()` OOMs | Already a base-script dep; needed ONLY if native `page_range` batching is insufficient [VERIFIED: base script imports] |
| `markdownlint-cli` | npm, already repo convention | Final `--fix` pass on the consolidated/split markdown | Repo already mandates markdownlint for all generated `.md` [VERIFIED: `mentor/reference.md:3-8`] |

### Supporting

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| stdlib `argparse` | 3.10+ | CLI args (`<pdf>`, `--slug`, `--out`) | Always — mirror `roadmap_fetch.py` style (D-12) |
| stdlib `pathlib`, `subprocess`, `os`, `gc` | 3.10+ | Paths, lint subprocess, env guards, memory cleanup | Always — already used by base script |

**Removed from base script:** `questionary` (D-12 — interactive select replaced by `argparse`).

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Structured-model split (`iterate_items`) | Post-process concatenated markdown headings (regex on `^#`) | Loses `level` precision + native page provenance; reintroduces parsing fragility. The model already gives `level` and `page_no` deterministically — prefer it. [CITED: docling-core document.py] |
| pypdf 1-page chunking (base script) | docling native `page_range=(s,e)` batches | Native page_range preserves cross-page structure AND real page numbers; pypdf split destroys both. [VERIFIED: docling `convert(page_range=...)`] |
| `HierarchicalChunker` | Manual `iterate_items` split | Chunker is tuned for RAG token windows, not "one file per chapter"; it may over-split a chapter. Use manual iteration for D-09's chapter granularity. [CITED: docling chunking examples] |

**Installation (opt-in, isolated — D-05/D-07):**

```bash
python -m venv .venv-pdf
.\.venv-pdf\Scripts\activate        # Windows PowerShell
pip install -r requirements-pdf.txt  # docling + pypdf
npm install -g markdownlint-cli      # if not already present
```

`requirements-pdf.txt` (suggested name — Claude's discretion):

```text
docling>=2.104.0
pypdf>=4.0
```

**Version verification:** `docling` latest = **2.104.0**, `requires_python: >=3.10,<4.0`
[VERIFIED: PyPI JSON, 2026-06-21]. Machine already has docling 2.81.0 installed under a uv-managed
Python 3.13 env — but `pypdf` was NOT found there, confirming the environment is ambiguous and a
**dedicated venv is mandatory** (do not rely on whatever `pip`/`python` resolves to globally).

## Architecture Patterns

### System Architecture Diagram

```
                    aluno tem livro?  (mentor pergunta — D-15)
                       /                          \
              ja em .md                         PDF
                  |                               |
         cola em livro/                  mentor mostra comando exato
         (zero deps — D-06)              OR dispara skill /converte-livro (D-13)
                  |                               |  (pre-aviso: demora / 0 tokens / progresso — D-14)
                  |                               v
                  |              +-------------------------------------+
                  |              |  scripts/<converter>.py  (CLI args) |
                  |              |  venv: docling + pypdf (opt-in)     |
                  |              +-------------------------------------+
                  |                               |
                  |             [env guards: OMP/MKL/OPENBLAS=1]  (D-12)
                  |                               v
                  |              DocumentConverter.convert(pdf,
                  |                  page_range=(1, N) whole-doc pass
                  |                  accelerator=CPU,num_threads=1)
                  |                               |
                  |                               v
                  |                  DoclingDocument (structured)
                  |                   |                       |
                  |          iterate_items()           prov[0].page_no
                  |          SECTION_HEADER/TITLE       per element  (D-10)
                  |          + .level                        |
                  |                   v                       |
                  |          DETERMINISTIC SPLIT  <-----------+
                  |          one .md per chapter,
                  |          <!-- page: N --> anchors   (D-09 + D-10)
                  |                   |
                  |          markdownlint --fix         (D-12)
                  v                   v
            .projetos/<slug>/livro/   <-- consolidated, chapter-split, page-anchored markdown
                  |
                  v
        mentor le livro/ como baseline durante tutoria  (D-01)
        "ve a pagina X do livro"  (D-10, multi-midia)
        divergencia livro x pesquisa -> APRENDIZADO.md datado  (D-03/D-04)
```

### Recommended Project Structure

```
scripts/
├── roadmap_fetch.py          # existing — UNTOUCHED, stdlib-only precedent
└── converte_livro.py         # NEW — opt-in docling CLI (name = discretion)
requirements-pdf.txt          # NEW — opt-in deps, isolated (D-07)
.claude/skills/
└── converte-livro/SKILL.md   # NEW — thin adapter pointing to mentor/ (D-13)
mentor/
├── novo-projeto.md           # EDIT — new optional bootstrap step (D-02, D-15)
├── tutor.md                  # EDIT — consult livro/ + page reference (D-10, D-01)
└── reference.md              # EDIT — add livro/ to .projetos/<slug>/ layout (D-08); APRENDIZADO divergence (D-04)
.projetos/<slug>/
└── livro/                    # NEW output dir (student artifact — accented PT preserved)
    ├── 01-<chapter-slug>.md
    └── 02-<chapter-slug>.md
```

### Pattern 1: Whole-document convert with controlled memory (replaces pypdf 1-page chunk)

**What:** One `convert()` over the whole PDF, memory bounded by accelerator threads + env guards.
**When to use:** Default path. Preserves cross-page headings (D-09) and native `page_no` (D-10).

```python
# Source: docling convert(page_range=...) + run_with_accelerator.py [CITED: docling document_converter.py, accelerator_options.py]
import os
os.environ["OMP_NUM_THREADS"] = "1"          # PRESERVE base-script guards (D-12)
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions

opts = PdfPipelineOptions()
opts.do_ocr = True                            # PRESERVE (base script)
opts.generate_picture_images = True           # PRESERVE (base script); best-effort figures (D-11)
opts.accelerator_options = AcceleratorOptions(num_threads=1, device=AcceleratorDevice.CPU)

converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
)
result = converter.convert(pdf_path)          # add page_range=(s,e) only as OOM fallback
doc = result.document
```

### Pattern 2: Deterministic chapter split by section header (D-09)

**What:** Iterate the structured model; start a new chapter file at each `TITLE`/`SECTION_HEADER`
at or above the cut level (H1 vs H2 = discretion).
**When to use:** Core of D-09. No LLM involved.

```python
# Source: docling iterate_items + SectionHeaderItem.level [CITED: docling-core document.py; docling xbrl_conversion.ipynb]
from docling_core.types.doc import DocItemLabel

CUT_LEVEL = 1  # H1 boundary; tune to H2 if chapters are level-2 (discretion D-09)

chapters, current = [], None
for item, _ in doc.iterate_items():
    label = getattr(item, "label", None)
    is_boundary = (
        label == DocItemLabel.TITLE
        or (label == DocItemLabel.SECTION_HEADER and getattr(item, "level", 99) <= CUT_LEVEL)
    )
    if is_boundary:
        current = {"title": item.text, "start_page": _page_of(item), "items": []}
        chapters.append(current)
    if current is not None:
        current["items"].append(item)
```

### Pattern 3: Per-chunk page anchor from provenance (D-10)

**What:** Each chapter (and optionally each major heading) gets a `<!-- page: N -->` marker pulled
from docling's element provenance — NOT from a manual page loop.
**When to use:** D-10. Replaces the base script's `---` separator.

```python
# Source: prov[0].page_no grouping [CITED: docling post_process_ocr_with_vlm.py]
def _page_of(item):
    if getattr(item, "prov", None):
        return item.prov[0].page_no      # 1-based page number, native from docling
    return None

# Emit at chapter start (and optionally before each H2):
#   <!-- page: 42 -->
```

**Alternative (whole-doc markdown with page breaks):** if you export the whole document to one
markdown blob, `export_to_markdown(page_break_placeholder="<!-- page: BREAK -->")` inserts a marker
at every page boundary deterministically — but it does NOT embed the page NUMBER, only marks the
break. For numbered anchors ("ve a pagina X"), prefer `prov[0].page_no` per Pattern 3.
[CITED: docling-core document.py export_to_markdown signature]

### Pattern 4: Preserve final markdownlint --fix (D-12)

```python
# Source: base script converter.py:109-125 — PRESERVE verbatim
subprocess.run(["markdownlint", "--fix", str(md_path)],
               capture_output=True, text=True, check=False, shell=True)  # shell=True for Windows
```

### Anti-Patterns to Avoid

- **pypdf 1-page chunk as the primary loop (base script).** It silently destroys D-09 (headings
  split across page boundary) and D-10 (`page_no` is always 1 inside a 1-page PDF). Keep page-range
  ONLY as an OOM fallback, batched (e.g. 10-20 pages), never 1 page.
- **Letting the LLM do the split or page numbering.** Violates D-09's explicit "deterministico, nao
  pela LLM" and the phase's guiding principle.
- **Stripping accents from the book markdown.** `livro/` is a STUDENT artifact -> accented Portuguese
  (or the book's source language) MUST be preserved (D-15 discretion; `mentor/reference.md:37`).
  Do NOT route the book text through ASCII-only normalization.
- **Mentor running docling silently.** D-15 forbids it: the mentor surfaces the command / fires the
  skill with the D-14 pre-warning, then consumes `livro/` once populated.
- **Adding docling to a global/shared requirements.** Breaks D-05/D-07 isolation; core stays stdlib.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| PDF text/layout extraction | Custom pdf parser | `docling` | OCR, layout, tables, reading order solved [VERIFIED] |
| Heading hierarchy detection | Font-size heuristics on raw text | `SectionHeaderItem.level` from docling | docling already classifies + levels headings [CITED: docling-core] |
| Page number per element | Manual page-loop bookkeeping | `item.prov[0].page_no` | Native provenance survives whole-doc conversion [CITED: docling] |
| Markdown formatting cleanup | Custom regex normalizer | `markdownlint --fix` | Already a repo convention [VERIFIED: reference.md] |
| Markdown serialization | Manual string building from items | `export_to_markdown(from_element, to_element, labels, page_no)` | Element-range + page-scoped slicing built in [CITED: docling-core] |

**Key insight:** docling's `DoclingDocument` already carries every signal this phase needs
(heading level, page number, label type) as first-class structured data. The deterministic work
(D-09/D-10) is reading those fields, not re-deriving them from text.

## Common Pitfalls

### Pitfall 1: std::bad_alloc / OOM during OCR
**What goes wrong:** docling's OCR/layout models exhaust memory on large books.
**Why it happens:** Default multi-threaded BLAS/OMP backends + whole-PDF OCR.
**How to avoid:** Keep the base script's env guards (`OMP_NUM_THREADS=1` etc.) AND set
`AcceleratorOptions(num_threads=1, device=CPU)`. If it still OOMs on a very large book, fall back to
`page_range` **batches** (e.g. 10-20 pages), merging the resulting `DoclingDocument`s — never 1 page.
**Warning signs:** `std::bad_alloc`, process killed mid-conversion.

### Pitfall 2: First run downloads ~2GB+ (torch + HF models)
**What goes wrong:** First conversion hangs for minutes with no obvious cause.
**Why it happens:** `pip install docling` pulls torch (>2GB); models download from Hugging Face on
first `convert()`.
**How to avoid:** This is exactly what D-14's pre-warning covers — the agent MUST tell the student
"vai demorar (download de modelos na 1a vez), nao consome tokens, roda local". Surface the
"pagina N de M" progress the script already prints.
**Warning signs:** Long silent first run; network activity to huggingface.co.

### Pitfall 3: Wrong Python / wrong venv picks up no deps
**What goes wrong:** `python scripts/converte_livro.py` runs under a Python where docling/pypdf
aren't installed (this machine has 3+ Python envs; docling found under uv-Python 3.13 but pypdf not).
**Why it happens:** Ambiguous global `python`/`pip` resolution.
**How to avoid:** Document explicit venv activation in the command the mentor surfaces (D-15) and in
the skill. Require Python 3.10+ (docling `requires_python`).
**Warning signs:** `ModuleNotFoundError: No module named 'docling'`.

### Pitfall 4: markdownlint not installed
**What goes wrong:** Final lint step fails.
**Why it happens:** `markdownlint-cli` is npm, separate from the Python venv.
**How to avoid:** Base script already handles `FileNotFoundError` gracefully — preserve that. There
is no `.markdownlint.json` in the repo, so it runs with defaults (consistent with current behavior).
**Warning signs:** `'markdownlint' not found`.

### Pitfall 5: Chapter cut level mismatch (H1 vs H2)
**What goes wrong:** Either one giant file (cut too high) or hundreds of tiny files (cut too low).
**Why it happens:** Books vary — some use a single TITLE per chapter, others H1=part / H2=chapter.
**How to avoid:** Make `CUT_LEVEL` a CLI flag (default 1). Print the detected heading histogram
(count by level) so the student/agent can pick. This is the D-09 discretion item.
**Warning signs:** 1 output file, or >50 output files for a normal book.

## Code Examples

See Patterns 1-4 above (all sourced). Additional structure inspection:

### Inspect heading histogram before choosing cut level
```python
# Source: docling xbrl_conversion.ipynb [CITED]
from collections import Counter
levels = Counter()
for item, _ in doc.iterate_items():
    if getattr(item, "label", None) and item.label.name in ("TITLE", "SECTION_HEADER"):
        levels[(item.label.name, getattr(item, "level", None))] += 1
print(levels)  # informs CUT_LEVEL choice
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| pypdf 1-page split + concat markdown (base script) | docling whole-doc `convert()` + `iterate_items` split | docling 2.x maturity | Preserves structure + native page numbers |
| Manual heading regex | `SectionHeaderItem.level` | docling-core | Deterministic, no parsing fragility |
| Agent improvises conversion | docling's own agent-skill: deterministic, script-prescribed flow | docling examples/agent_skill | Confirms D-09/D-13/D-14 design is the vendor-blessed pattern [CITED: docling SKILL.md] |

**Deprecated/outdated:**
- `questionary` interactive selection: removed per D-12 (CLI args instead).
- `use_legacy_annotations` param in `export_to_markdown`: deprecated — do not use.

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | The book's PDF is born-digital or OCR-able such that docling produces real `SECTION_HEADER` items (vs. flat text). Scanned books with no detectable structure would yield a poor split. | Patterns 2 | Medium — split degrades to one file; page anchors still work. Mitigate with heading-histogram check (Pitfall 5). |
| A2 | A single whole-document `convert()` fits in memory for a typical book with threads=1. | Pattern 1 | Medium — fall back to page_range batches. Validate on the student's actual book during execution. |
| A3 | The student/agent runs from a dedicated venv with deps installed (not the ambiguous global Python). | Pitfall 3 | Low — explicit venv instructions mitigate. |

## Open Questions

1. **Chapter cut level (H1 vs H2) — D-09 discretion.**
   - What we know: docling gives `level` per `SECTION_HEADER`; default cut = level 1.
   - What's unclear: which level == "chapter" varies per book.
   - Recommendation: CLI flag `--cut-level` (default 1) + print heading histogram. Decide at plan time.

2. **Page anchor granularity — D-10.**
   - What we know: `prov[0].page_no` available per element; `<!-- page: N -->` is the suggested format.
   - What's unclear: anchor once per chapter file, or also before each H2 / every page boundary.
   - Recommendation: at minimum at chapter start; consider per-major-heading so "ve a pagina X" is
     precise mid-chapter. Confirm format (HTML comment vs heading) with user — it's discretion.

3. **Merging `DoclingDocument`s across page_range batches (OOM fallback only).**
   - What we know: native whole-doc convert is preferred and usually sufficient.
   - What's unclear: clean API to concatenate per-batch documents while keeping global page numbers.
   - Recommendation: only investigate if A2 fails on the real book; not needed for the happy path.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python 3.10+ | converter script | Yes (multiple: uv-3.13 + others) | 3.13 found | — (require venv) |
| `docling` | conversion | Partially (2.81.0 under uv-Python; not in a clean venv) | 2.81.0 installed / 2.104.0 latest | Install into dedicated venv |
| `pypdf` | OOM-fallback batching | NOT found in checked env | — | `pip install pypdf` into venv |
| `markdownlint-cli` (npm) | final lint | Unverified here (repo convention assumes present) | — | Script already degrades gracefully (FileNotFoundError) |
| torch (+ HF models) | docling pipeline | Pulled transitively by docling (~2GB+, downloaded first run) | — | None — D-14 pre-warns student |
| Internet (first run) | HF model download | Assumed | — | Pre-download models / warn |

**Missing dependencies with no fallback:** none that block — all installable into the opt-in venv.
**Missing dependencies with fallback:** `pypdf` (install on demand); `markdownlint-cli` (graceful skip).

## Validation Architecture

> nyquist_validation is enabled (config.json `workflow.nyquist_validation: true`).

The phase's verifiable contract is **deterministic conversion output**, which is testable without an
LLM. Because docling itself is heavy/opt-in, tests split into (a) pure-logic tests on the split/anchor
functions using a synthetic in-memory `DoclingDocument` (fast, no docling pipeline run), and (b) one
opt-in golden-file smoke test on a tiny sample PDF (marked slow / skipped when docling absent).

### Test Framework
| Property | Value |
|----------|-------|
| Framework | `pytest` (none currently in repo — Wave 0 introduces it for this opt-in script ONLY; core stays stdlib/test-free) |
| Config file | none — see Wave 0 |
| Quick run command | `python -m pytest tests/test_converte_livro.py -x -q` (logic tests, no docling pipeline) |
| Full suite command | `python -m pytest tests/ -q` (includes `@pytest.mark.slow` golden-PDF smoke) |

### Phase Requirements -> Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| D-09 | Split starts a new chapter at each TITLE/SECTION_HEADER<=cut_level | unit | `pytest tests/test_converte_livro.py::test_split_by_heading -x` | Wave 0 |
| D-09 | N output files == N boundary headings | unit | `pytest tests/test_converte_livro.py::test_chapter_count -x` | Wave 0 |
| D-10 | Each chapter file contains a `<!-- page: N -->` anchor with N from prov | unit | `pytest tests/test_converte_livro.py::test_page_anchor_present -x` | Wave 0 |
| D-10 | Page number equals element `prov[0].page_no` | unit | `pytest tests/test_converte_livro.py::test_page_anchor_value -x` | Wave 0 |
| D-12 | Memory env guards set before docling import | unit | `pytest tests/test_converte_livro.py::test_env_guards -x` | Wave 0 |
| D-12 | markdownlint invoked with `--fix` (subprocess mocked) | unit | `pytest tests/test_converte_livro.py::test_lint_called -x` | Wave 0 |
| D-15 | Accents preserved in book markdown (no ASCII normalization) | unit | `pytest tests/test_converte_livro.py::test_accents_preserved -x` | Wave 0 |
| end-to-end | Tiny sample PDF -> >=1 chapter file with anchor (golden smoke) | slow/manual | `pytest tests/ -m slow -q` (skips if docling not installed) | Wave 0 |
| method | `mentor/*.md` edits consistent (no method dup in adapters) | existing harness | `sh scripts/check-consistencia.sh` (repo's permanent checker) | Yes |

### Sampling Rate
- **Per task commit:** `python -m pytest tests/test_converte_livro.py -x -q` (logic only, sub-second).
- **Per wave merge:** full suite incl. `-m slow` golden PDF (run once where docling venv exists).
- **Phase gate:** logic suite green + one successful golden-PDF smoke + `check-consistencia.sh` exit 0
  for any `mentor/` edits, before `/gsd-verify-work`.

### Wave 0 Gaps
- [ ] `tests/test_converte_livro.py` — unit tests over split/anchor/env/lint/accents using a synthetic
  `DoclingDocument` (build minimal items in-memory; no pipeline run).
- [ ] `tests/conftest.py` — fixture building the synthetic document + `@pytest.mark.slow` skip-if
  docling missing.
- [ ] `tests/fixtures/sample.pdf` — tiny 2-3 page PDF with 2 headings for the golden smoke.
- [ ] Framework install: `pip install pytest` into the opt-in venv (NOT into core).
- [ ] Decision: keep tests OUT of the stdlib-only core's "zero setup" promise — they live with the
  opt-in script and run only when the PDF venv exists.

## Security Domain

> `security_enforcement` not set in config (treated as enabled), but this is a LOCAL, single-user CLI
> that reads a file path the user provides and writes markdown — no auth, no network input surface
> (model download is outbound to HF only), no untrusted multi-tenant data. Threat surface is minimal.

### Applicable ASVS Categories
| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V5 Input Validation | yes (light) | Validate `--slug` is safe path component (kebab-case, no `..`/separators) before writing under `.projetos/<slug>/livro/`; validate PDF path exists |
| V12 File / Resource | yes (light) | Write only inside `.projetos/<slug>/livro/`; clean up temp PDF (base script already does) |
| V2/V3/V4 Auth/Session/Access | no | Local single-user CLI, no auth |
| V6 Cryptography | no | No secrets, no crypto |

### Known Threat Patterns for {local Python CLI}
| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Path traversal via `--slug` | Tampering | Reject slugs containing path separators / `..`; whitelist `[a-z0-9-]` (matches existing slug convention `mentor/novo-projeto.md:93`) |
| `subprocess(..., shell=True)` on Windows | Injection | Args are fixed literals + a controlled path; keep the list form, do not interpolate user text into a shell string |
| Malicious/huge PDF (resource exhaustion) | DoS | threads=1 + optional `max_num_pages`/`max_file_size` (docling `convert()` supports both) |

## Sources

### Primary (HIGH confidence)
- Context7 `/docling-project/docling-core` — `ProvenanceItem.page_no`, `SectionHeaderItem.level`,
  `export_to_markdown(from_element,to_element,labels,page_no,page_break_placeholder)`, `DocItemLabel`.
- Context7 `/docling-project/docling` — `convert(page_range=...)`, `AcceleratorOptions(device,num_threads)`,
  `iterate_items()`, `prov[0].page_no` grouping, `HierarchicalChunker`, agent-skill example.
- PyPI `docling` JSON — latest 2.104.0, `requires_python >=3.10,<4.0` (verified 2026-06-21).
- In-repo: `converter.py` (base script), `roadmap_fetch.py` (style precedent), `mentor/reference.md`
  (markdownlint + accent convention), `mentor/novo-projeto.md` (bootstrap integration point).

### Secondary (MEDIUM confidence)
- https://docling-project.github.io/docling/getting_started/installation/ — torch >2GB, first-run
  model download from Hugging Face.
- https://raw.githubusercontent.com/docling-project/docling/main/docs/examples/agent_skill/docling-document-intelligence/SKILL.md
  — vendor's deterministic, script-prescribed agent flow (corroborates D-09/D-13/D-14).

### Tertiary (LOW confidence)
- Local `pip index versions docling` / `pip show pypdf` — environment is ambiguous (multiple Python
  installs); used only to confirm a dedicated venv is needed, not as authoritative install state.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — docling API verified via Context7 source + PyPI version.
- Architecture (split + page anchor): HIGH — `iterate_items`/`level`/`prov.page_no`/`page_range` all
  confirmed in docling/docling-core source.
- Pitfalls (memory, first-run, env): MEDIUM-HIGH — install footprint from official docs; OOM behavior
  inferred from base-script guards + accelerator API (validate on the real book at execution).
- Cut-level / anchor-granularity: MEDIUM — verified the mechanism; the exact policy is a discretion
  decision for the plan.

**Research date:** 2026-06-21
**Valid until:** ~2026-07-21 (docling is fast-moving — re-verify version + `export_to_markdown`
signature if planning slips beyond 30 days).
