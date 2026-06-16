# Phase 5: Persona e feedback (metodo.md + debug.md) - Pattern Map

**Mapped:** 2026-06-15
**Files analyzed:** 4 (2 MODIFIED docs + 2 CREATED scripts)
**Analogs found:** 4 / 4 (all exact)

> DOC-EDITING + harness-clone phase. No application code. "Pattern to copy from" means:
> (a) for the Wave 0 scripts -> the EXACT existing script files to clone;
> (b) for the doc edits -> the literal headings/sections that are the edit anchors, plus
> the in-repo prose conventions already used by Phases 2/3/4 (hyperlink-cite, source-single,
> anti-leak scoped to fenced blocks, rigid leveza guardrail).

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `.planning/phases/05-.../scripts/extract-fenced.sh` (CREATE) | test-harness (fenced extractor) | transform (stdin->stdout filter) | `.planning/phases/04-.../scripts/extract-fenced.sh` | exact (clone verbatim) |
| `.planning/phases/05-.../scripts/check-phase5.sh` (CREATE) | test-harness (static gate) | batch (grep PASS/FAIL) | `.planning/phases/04-.../scripts/check-phase4.sh` | exact (clone shell scaffold, re-author checks) |
| `mentor/metodo.md` (MODIFY) | doc / persona-conduct | doc-edit (in-place anchored insert) | self + Phase 2/3/4 weave conventions | exact (anchors live in file) |
| `mentor/debug.md` (MODIFY) | doc / procedure-owner | doc-edit (non-destructive overlay) | self + Phase 4 overlay pattern | exact (anchors live in file) |

## Pattern Assignments

### `.planning/phases/05-.../scripts/extract-fenced.sh` (CREATE — clone verbatim)

**Analog:** `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/extract-fenced.sh`
(also identical at `.planning/phases/02-templates-e-sintaxe-reference-md/scripts/extract-fenced.sh`)

**read_first:** `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/extract-fenced.sh`

**Action:** Copy the file BYTE-FOR-BYTE into the Phase 5 scripts dir. The script is already
generic — it takes a filename arg and only differs by default. Do NOT change the awk logic.
The full content to clone (26 lines):

```sh
#!/usr/bin/env sh
# extract-fenced.sh -- imprime SO o conteudo dentro de blocos cercados (```), sem as cercas.
#
# Uso: sh extract-fenced.sh [arquivo.md]   (default: mentor/reference.md)
#
# Porque existe: o grep negativo anti-leak (CONS-01) precisa rodar SO contra o conteudo
# que vira artefato do aluno (dentro dos blocos ```). A prosa LEGITIMA de reference.md
# pode nomear frameworks (ex: "backward design"); rodar o grep no doc inteiro daria
# falso-positivo. Este extrator isola o subconjunto correto.
#
# Logica (toggle de estado): percorre linha a linha; ao encontrar uma linha cujo conteudo
# (apos espacos iniciais) comeca com tres crases, alterna o flag `inside` e PULA a cerca.
# Quando `inside` esta ligado e a linha NAO e uma cerca, imprime a linha.

FILE="${1:-mentor/reference.md}"

if [ ! -f "$FILE" ]; then
  echo "extract-fenced.sh: arquivo nao encontrado: $FILE" >&2
  exit 2
fi

awk '
  /^[[:space:]]*```/ { inside = !inside; next }
  inside { print }
' "$FILE"
```

**Note:** The default of `mentor/reference.md` is harmless — `check-phase5.sh` always passes
an explicit file arg (`"$DIR/extract-fenced.sh" "$REF"` style). Clone unchanged.

---

### `.planning/phases/05-.../scripts/check-phase5.sh` (CREATE — clone scaffold, re-author checks)

**Analog:** `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/check-phase4.sh`

**read_first:** `.planning/phases/04-gate-e-retrieval-fecha-marco-md-tutor-md/scripts/check-phase4.sh`
AND `.planning/phases/05-.../05-RESEARCH.md` §"Validation Architecture" (the V-01..V-18 table
and the Code Examples block — those are the authoritative check bodies).

**What to KEEP VERBATIM from the analog (lines 18-61):** the file-var/`fails` setup and the
three check helpers. Copy these unchanged, only swapping the doc-path vars:

```sh
DIR=$(dirname "$0")
MET="mentor/metodo.md"
DBG="mentor/debug.md"
FUN="mentor/fundamentos.md"
REF="mentor/reference.md"
TUT="mentor/tutor.md"
FCH="mentor/fecha-marco.md"
fails=0

# conta ocorrencias de um padrao num arquivo (0 se nada casa)
count() {
  rg -c "$1" "$2" 2>/dev/null || echo 0
}

# criterio positivo: PASS quando o valor observado >= o minimo esperado
check_min() {
  label="$1"; val="$2"; min="$3"
  if [ "$val" -ge "$min" ]; then
    printf 'PASS  %-16s got=%s need>=%s\n' "$label" "$val" "$min"
  else
    printf 'FAIL  %-16s got=%s need>=%s\n' "$label" "$val" "$min"
    fails=$((fails + 1))
  fi
}

# criterio negativo (anti-leak): PASS quando o valor observado == 0
check_zero() {
  label="$1"; val="$2"
  if [ "$val" -eq 0 ]; then
    printf 'PASS  %-16s got=%s need=0\n' "$label" "$val"
  else
    printf 'FAIL  %-16s got=%s need=0\n' "$label" "$val"
    fails=$((fails + 1))
  fi
}

# checagem booleana: PASS quando o comando rg -q acha o padrao (exit 0)
check_has() {
  label="$1"; pat="$2"; file="$3"
  if rg -q "$pat" "$file" 2>/dev/null; then
    printf 'PASS  %-16s found in %s\n' "$label" "$file"
  else
    printf 'FAIL  %-16s NOT found in %s\n' "$label" "$file"
    fails=$((fails + 1))
  fi
}
```

**ANCHOR-RESOLVE pattern to clone (analog lines 110-118):** copy this block STRUCTURE,
swapping the three headings to the Phase 5 D-09 targets (all three VERIFIED present in repo
today — reference.md:406, tutor.md:37, fecha-marco.md:12). Grep the LITERAL HEADING, never a
reconstructed slug (the GRR slug has `:`/`"`/`->` and is fragile — A1 / Pitfall 4):

```sh
# V-16 (ANCHOR-RESOLVE): as 3 ancoras D-09 resolvem como heading real no dono
if rg -q '^### Sintaxe nova de verdade' "$REF" 2>/dev/null && \
   rg -q '^## Passo 1 — Recuperacao ativa' "$TUT" 2>/dev/null && \
   rg -q '^## Passo 1 — Mastery gate' "$FCH" 2>/dev/null; then
  printf 'PASS  %-16s as 3 ancoras D-09 resolvem\n' "V-16"
else
  printf 'FAIL  %-16s ancora D-09 ausente\n' "V-16"
  fails=$((fails + 1))
fi
```

**ANTI-LEAK pattern to clone (analog lines 120-126):** copy the `extract-fenced.sh | rg -c`
+ `check_zero` shape. The ONLY change vs Phase 4 is the `LEAK_PAT` — extend it with the new
Phase 5 jargon (Hattie/feed-*/formativo/auto-explicacao) and keep `retrieval practice`/
`testing effect` as PHRASES (never bare `retrieval`, which is a legit contract label). Run it
against BOTH edited docs:

```sh
# V-17 (CONS-01 anti-leak): NENHUM jargao de framework DENTRO de bloco cercado -> 0.
#   Forma de FRASE quando o token isolado e ambiguo (retrieval practice, nao retrieval solto).
LEAK_PAT='SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect|feed-up|feed-back|feed-forward|Hattie|formativ|auto-explicacao'
leak_met=$(sh "$DIR/extract-fenced.sh" "$MET" | rg -c "$LEAK_PAT" 2>/dev/null || echo 0)
leak_dbg=$(sh "$DIR/extract-fenced.sh" "$DBG" | rg -c "$LEAK_PAT" 2>/dev/null || echo 0)
check_zero "ANTI-LEAK-METODO" "$leak_met"
check_zero "ANTI-LEAK-DEBUG"  "$leak_dbg"
```

**POSITIVE checks to author (from RESEARCH §Code Examples + V-01..V-15, V-18):** use the
`check_min "LABEL" "$(count 'PAT' FILE)" MIN` idiom verbatim. The planner should encode each
V-row. Representative set (copy patterns from RESEARCH:434-446):

```sh
# CONS-01 (V-01..V-04): metodo.md cita fundamentos.md (1a ponte) + corpo + FUND-03 + espelho
check_min "V-01-link"   "$(count 'fundamentos\.md' "$MET")" 1
check_min "V-02-corpo"  "$(count 'jargao|nunca .*ao aluno|nunca .*citad' "$MET")" 1
check_min "V-03-fund03" "$(count 'interno|nunca .*lido pelo aluno|injetad' "$MET")" 1
check_min "V-04-espelho" "$(count 'jargao.*aluno|framework.*aluno' "$MET")" 1
# AVAL-05 (V-05..V-07): novo passo + guardrail literal + fronteira fecha-marco
check_min "V-05-autoexp" "$(count 'auto-explicacao|me explica por que|explicar.*antes de curar' "$MET")" 1
check_min "V-06-guard"   "$(count 'exatamente 1|checklist ou rubrica|esta errado' "$MET")" 1
check_min "V-07-front"   "$(count 'fecha-marco' "$MET")" 1
# AVAL-06 (V-08..V-10): 3 lentes + PISTA=feed-forward + 6 passos preservados
check_min "V-08-lentes"  "$(count 'feed-up|feed-back|feed-forward' "$DBG")" 3
check_min "V-09-pista"   "$(count 'PISTA.*feed-forward|feed-forward.*PISTA|PISTA.*sem .*resposta' "$DBG")" 1
check_min "V-10-6passos" "$(count '^### [1-6]\.' "$DBG")" 6
# Criterio 4 (V-11..V-13): ciclo linka GRR/retrieval/gate
check_min "V-11-grr"     "$(count 'reference\.md' "$MET")" 1
check_min "V-12-retr"    "$(count 'tutor\.md|/tutor' "$MET")" 1
check_min "V-13-gate"    "$(count 'fecha-marco\.md|/fecha-marco' "$MET")" 1
# D-07 (V-15): ponteiro curto nomeia "feedback tri-partido" + link /debug
check_min "V-15-ptr"     "$(count 'feedback tri-partido' "$MET")" 1
# V-18 defensivo (P12 anti-drift): jargao novo NAO vaza para adaptadores
check_min_zero_note="V-18 roda rg sobre AGENTS.md/.claude/ -> 0 (defensivo)"
```

**Tail to clone (analog lines 128-129):**

```sh
echo "== $fails fail(s) =="
exit $fails
```

**Baseline expectation (same convention as Phase 2/4, RESEARCH:544-545):** before edits, the
POSITIVE checks FAIL (expected); V-16 (ANCHOR-RESOLVE — 3 headings already exist) and V-17/V-18
(anti-leak baseline 0) PASS.

---

### `mentor/metodo.md` (MODIFY — anchored inserts, no restructure)

**Analog:** the file itself + the in-repo weave conventions (Phase 2 hyperlink-cite; Phase 3
anti-leak nuance; Phase 4 rigid leveza guardrail). All edit anchors are LITERAL headings that
exist today (verified by read).

**read_first:** `mentor/metodo.md` (full), `mentor/fundamentos.md` (preamble 3-8 = FUND-03;
table heading line 41), `mentor/reference.md` (GRR heading 406), `mentor/tutor.md` (37),
`mentor/fecha-marco.md` (12), `.planning/phases/03-.../03-CONTEXT.md` (anti-leak nuance).

**Edit anchor 1 — CONS-01 body rule (D-01 affirmative + D-02 FUND-03):**
Insert a short new rule right after the `## Regra de ouro` section (metodo.md:12-16) — earliest
point the agent reads. This is metodo.md's FIRST reference to `fundamentos.md`. Existing pattern
to mirror: a rule lives in the body and is mirrored short in the Anti-padroes list (the Regra
de ouro at line 12-16 -> mirrored as "Preencher o `TODO(human)` pelo aluno." at line 143).
Form (RESEARCH:200-204; text is Claude's discretion):

```markdown
A fundamentacao guia a sua conduta, nunca vira conteudo: voce APLICA as boas praticas,
mas NUNCA cita o nome do framework ao aluno na sessao. O "porque" teorico (interno) esta
em [fundamentos.md](fundamentos.md) — doc do agente, jamais lido pelo aluno nem injetado
na sessao.
```

**Edit anchor 2 — CONS-01 mirror (D-01):**
Section `## Anti-padroes (NUNCA faca)` — LITERAL heading at metodo.md:141, a bulleted list
(lines 143-166). Add ONE short imperative item, mirroring the existing terse style of those
bullets (e.g. line 143 `- Preencher o TODO(human) pelo aluno.`). Form (RESEARCH:207):

```markdown
- Citar jargao de framework (Bloom, CLT, retrieval...) ao aluno na sessao — a teoria guia voce, nao e despejada nele.
```

**Edit anchor 3 — AVAL-05 formative check (D-03 + D-04):**
Section `## Gate de curadoria — "so depois de funcionar"` — LITERAL heading at metodo.md:64.
Today: 3 numbered steps (66-72) + "Ordem sagrada" line (74-75). The gate currently reads:
step 2 = "Quando o codigo funciona E passa no criterio de 'done', ai sim abra a curadoria"
(line 68). D-03 inserts a NEW step BETWEEN step 2 (code works) and step 3 (curadoria/melhorias)
— i.e. before the 1-3 improvements open. The new step = exactly 1 self-explanation question
("me explica por que isso funciona"); only advance to curadoria if the student can explain,
else gap -> back to concept. D-04 writes the rigid guardrail + boundary note.
The rigid-leveza guardrail STYLE is inherited from Phase 4 `fecha-marco.md` ("Mantenha leve...
Nao vire quiz nem checklist gigante"). Guardrail + boundary literals to write (RESEARCH:209-212):

```markdown
Guardrail: check formativo = exatamente 1 pergunta de auto-explicacao; se virou checklist
ou rubrica, esta errado.
Fronteira: o gate de DOMINIO por marco (sintese/transferencia) mora em
[fecha-marco.md](fecha-marco.md) — aqui e o micro-check do gate de curadoria por passo,
nao o mastery gate por marco.
```

**Edit anchor 4 — D-07 forense pointer (stays short):**
Section `## Protocolo de forense (quando o aluno erra)` — LITERAL heading at metodo.md:77.
Today: 6-step summary (81-86) + the "travado ha mais de 10 minutos" line (88-89). D-07 keeps
it a SHORT pointer; add AT MOST 1 line naming "feedback tri-partido" + link to `/debug`. Do
NOT copy the tri-partite definition (that lives only in debug.md — fonte-unica; Pitfall 1).

**Edit anchor 5 — Criterio 4 named cycle (D-08 inline + D-09 exactly 3 links):**
Section `## Conduta por marco (ciclo)` — LITERAL heading at metodo.md:32; 5 numbered items
(34-62). Annotate INLINE where each stage already occurs (no new overview block):
- **GRR** -> step 3 (line 48-58) already says `inverta para "eu faco -> voce faz"` — name
  "GRR 3 fases" + link `[reference.md](reference.md)` (owner of GRR syntax, heading
  `### Sintaxe nova de verdade` at reference.md:406). Link the doc/heading; the exact slug is
  fragile (verify by 1 click at the gate — A1).
- **retrieval** -> cycle opening / "Onde voce esta no fluxo" (line 22 mentions `/tutor`) —
  name "retrieval (recuperacao ativa)" + link `[tutor.md](tutor.md)` (heading
  `## Passo 1 — Recuperacao ativa` at tutor.md:37).
- **gate** -> tie to `## Fechamento de marco` (line 132, mentions `/fecha-marco` at 139) —
  name "mastery gate" + link `[fecha-marco.md](fecha-marco.md)` (heading
  `## Passo 1 — Mastery gate` at fecha-marco.md:12).
- Scope is CLOSED at these 3 — do NOT name backward design / "primeiro done leve" (rejected D-09).

---

### `mentor/debug.md` (MODIFY — non-destructive Hattie overlay)

**Analog:** the file itself + Phase 4/D-08 overlay pattern (annotate, don't restructure).

**read_first:** `mentor/debug.md` (full), `mentor/fundamentos.md` (Hattie line in table,
~49), `.planning/phases/05-.../05-RESEARCH.md` §Pattern 2 (overlay example).

**Edit anchor 1 — D-05 Hattie overlay over the 6 steps:**
Section `## O protocolo (6 passos)` — LITERAL heading at debug.md:14. The six sub-headings
exist today: `### 1. Observar` (16), `### 2. Isolar` (30), `### 3. Hipoteses` (41),
`### 4. Testar` (52), `### 5. Corrigir` (64), `### 6. Documentar` (76). KEEP all 6 (overlay,
not rewrite — Pitfall 5; V-10 counts `^### [1-6]\.` == 6). Add a blockquote/note mapping the
6 steps to the 3 Hattie lenses, and optionally a `(feed-up/back/forward)` label per sub-heading.
Mapping (D-05, fixed): feed-up (Aonde vou?) = Observar · feed-back (Como estou indo?) =
Isolar+Hipoteses+Testar · feed-forward (Para onde a seguir?) = Corrigir+PISTA+Documentar.
Form (RESEARCH:216-225):

```markdown
> Os 6 passos sao um ciclo de feedback acionavel em 3 lentes (Hattie & Timperley):
> feed-up (Aonde vou?) = Observar · feed-back (Como estou?) = Isolar+Hipoteses+Testar ·
> feed-forward (Para onde a seguir?) = Corrigir+PISTA+Documentar.
```

**Edit anchor 2 — D-06 PISTA = feed-forward:**
Inside `### 5. Corrigir`, at the existing line "Se estiver travado ha mais de 10 minutos,
ofereca a pista gradual (do scaffold) ou a resposta com explicacao." (debug.md:73). Frame the
PISTA there as feed-forward: "PISTA = feed-forward: aponta a direcao do proximo passo SEM
entregar a resposta." Do NOT move/redefine the PISTA scaffold syntax — that stays in
`reference.md`/`metodo.md` (Pitfall: don't recut; D-06 only names the ROLE).

## Shared Patterns

### Source-single (hyperlink-cite, never duplicate theory)
**Source convention:** `.planning/codebase/ARCHITECTURE.md`; established in Phase 2.
**Apply to:** every edit in this phase. New theory is NOT written here. metodo.md/debug.md cite
owner docs (`fundamentos.md`, `reference.md`, `tutor.md`, `fecha-marco.md`) by hyperlink.
The tri-partite forense definition lives ONLY in debug.md; metodo.md gets a pointer (D-07).

### Anti-leak scoped to fenced blocks (CONS-01)
**Source pattern:** `check-phase4.sh:120-126` + `extract-fenced.sh` (Phase 2/4).
**Apply to:** the V-17 anti-leak check only. The PROSE of metodo.md/debug.md MAY name frameworks
and link fundamentos.md (it is read by the agent). The anti-leak runs ONLY over fenced-block
content (student artifacts). Never grep the whole doc (Pitfall 3 false-positive).

### Rigid leveza guardrail (literal "exatamente 1...")
**Source pattern:** Phase 4 `fecha-marco.md` leveza guardrail + `check-phase4.sh` V-11
`exatamente 1` idiom. Phase 3 D-04 used the same rigid-guardrail move.
**Apply to:** D-04 in metodo.md ("check formativo = exatamente 1 pergunta de auto-explicacao;
se virou checklist ou rubrica, esta errado"). The check greps this literal (V-06).

### ANCHOR-RESOLVE on literal heading, not slug
**Source pattern:** `check-phase4.sh:110-118` (introduced Phase 4 for the SDT slug).
**Apply to:** every D-09 link (V-16). Grep the literal heading (`^### Sintaxe nova de verdade`,
`^## Passo 1 — Recuperacao ativa`, `^## Passo 1 — Mastery gate`) to prove the target exists;
confirm the exact `#slug` by 1 manual click at the phase gate (GRR slug is fragile — A1).

### Mirror-rule (body affirmative + short checklist echo)
**Source pattern:** metodo.md itself — Regra de ouro (body, 12-16) mirrored as a terse
Anti-padroes bullet (143). **Apply to:** D-01 (CONS-01 lives as a body rule + 1 mirror bullet).

## No Analog Found

None. Every file has an exact in-repo analog:
- Both Wave 0 scripts are proven clones (Phase 2 AND Phase 4).
- Both doc edits target literal headings that exist in the current repo (verified by read),
  and follow weave conventions already established across Phases 2/3/4.

## Metadata

**Analog search scope:** `.planning/phases/02-*/scripts/`, `.planning/phases/04-*/scripts/`,
`mentor/*.md`.
**Files scanned:** check-phase4.sh, extract-fenced.sh (P4), check-phase2.sh + extract-fenced.sh
(P2, confirmed identical extractor), metodo.md, debug.md; anchor headings verified in
reference.md / tutor.md / fecha-marco.md / fundamentos.md.
**Anchor-resolve check (run 2026-06-15):** all 4 owner headings present
(reference.md:406, tutor.md:37, fecha-marco.md:12, fundamentos.md:41).
**Pattern extraction date:** 2026-06-15
