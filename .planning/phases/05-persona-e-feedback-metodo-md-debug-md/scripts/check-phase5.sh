#!/usr/bin/env sh
# check-phase5.sh -- smoke-test estatico (gate da Fase 5).
#
# Roda os comandos rg da tabela "Per-Task Verification Map" (05-VALIDATION.md) contra
# mentor/metodo.md, mentor/debug.md e os docs donos (reference.md, tutor.md, fecha-marco.md),
# imprime PASS/FAIL por criterio e retorna exit != 0 se qualquer checagem falhar.
#
# Tres familias de checagem (clonadas verbatim de check-phase4.sh):
#   - check_min  LABEL  COUNT  MIN   -> PASS quando COUNT >= MIN (criterios positivos)
#   - check_zero LABEL  COUNT         -> PASS quando COUNT == 0  (anti-leak / anti-drift)
#   - check_has  LABEL  PAT   FILE    -> PASS quando rg -q acha o padrao (ANCHOR/CONTRACT)
#
# Nota sobre o baseline: ANTES das edicoes dos planos 02/03, varias checagens POSITIVAS
# vao FALHAR -- isso e esperado e correto, mesma convencao das Fases 2 e 4. So V-16
# (ANCHOR-RESOLVE, as 3 headings ja existem em reference.md/tutor.md/fecha-marco.md), V-17
# (ANTI-LEAK, baseline 0) e V-18 (ANTI-DRIFT adaptadores, baseline 0) passam no baseline.
# Este script e o gate FINAL desde o Wave 0 -- nenhum plano posterior edita este arquivo.

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

echo "== Phase 5 static smoke-test =="

# CONS-01 (metodo.md): cita fundamentos.md (1a ponte) + corpo + FUND-03 + espelho
check_min "V-01-link"    "$(count 'fundamentos\.md' "$MET")" 1
check_min "V-02-corpo"   "$(count 'jargao|nunca .*ao aluno|nunca .*citad' "$MET")" 1
check_min "V-03-fund03"  "$(count 'interno|nunca .*lido pelo aluno|injetad' "$MET")" 1
check_min "V-04-espelho" "$(count 'jargao.*aluno|framework.*aluno' "$MET")" 1

# AVAL-05 (metodo.md): novo check formativo + guardrail literal + fronteira fecha-marco
check_min "V-05-autoexp" "$(count 'auto-explicacao|me explica por que|explicar.*antes de curar' "$MET")" 1
check_min "V-06-guard"   "$(count 'exatamente 1|checklist ou rubrica|esta errado' "$MET")" 1
check_min "V-07-front"   "$(count 'fecha-marco' "$MET")" 1

# AVAL-06 (debug.md): 3 lentes Hattie + PISTA=feed-forward + 6 passos preservados
check_min "V-08-lentes"  "$(count 'feed-up|feed-back|feed-forward' "$DBG")" 3
check_min "V-09-pista"   "$(count 'PISTA.*feed-forward|feed-forward.*PISTA|PISTA.*sem .*resposta' "$DBG")" 1
check_min "V-10-6passos" "$(count '^### [1-6]\.' "$DBG")" 6

# Criterio 4 (metodo.md): ciclo linka GRR (reference) / retrieval (tutor) / gate (fecha-marco)
check_min "V-11-grr"     "$(count 'reference\.md' "$MET")" 1
check_min "V-12-retr"    "$(count 'tutor\.md|/tutor' "$MET")" 1
check_min "V-13-gate"    "$(count 'fecha-marco\.md|/fecha-marco' "$MET")" 1

# V-14: os 5 itens do ciclo preservados. Isola a secao "## Conduta por marco (ciclo)"
#   (do heading ate o proximo "## ") e conta as linhas que comecam com "[1-5]." (== 5).
c14=$(awk '/^## Conduta por marco \(ciclo\)/{f=1;next} /^## /{f=0} f && /^[1-5]\./{n++} END{print n+0}' "$MET")
check_min "V-14-5itens"  "$c14" 5

# D-07 (metodo.md): ponteiro curto nomeia "feedback tri-partido"
check_min "V-15-ptr"     "$(count 'feedback tri-partido' "$MET")" 1

# V-16 (ANCHOR-RESOLVE): as 3 ancoras D-09 resolvem como heading LITERAL no dono.
#   Grep do heading literal, nunca um slug reconstruido (o slug GRR e fragil -- A1 / Pitfall 4).
if rg -q '^### Sintaxe nova de verdade' "$REF" 2>/dev/null && \
   rg -q '^## Passo 1 — Recuperacao ativa' "$TUT" 2>/dev/null && \
   rg -q '^## Passo 1 — Mastery gate' "$FCH" 2>/dev/null; then
  printf 'PASS  %-16s as 3 ancoras D-09 resolvem\n' "V-16"
else
  printf 'FAIL  %-16s ancora D-09 ausente\n' "V-16"
  fails=$((fails + 1))
fi

# V-17 (CONS-01 anti-leak): NENHUM jargao de framework DENTRO de bloco cercado -> deve ser 0.
#   Roda SO sobre o conteudo cercado (via extract-fenced.sh), nunca sobre a prosa do doc inteiro.
#   Forma de FRASE quando o token solto e ambiguo ("retrieval practice", nao "retrieval").
LEAK_PAT='SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect|feed-up|feed-back|feed-forward|Hattie|formativ|auto-explicacao'
leak_met=$(sh "$DIR/extract-fenced.sh" "$MET" | rg -c "$LEAK_PAT" 2>/dev/null || echo 0)
leak_dbg=$(sh "$DIR/extract-fenced.sh" "$DBG" | rg -c "$LEAK_PAT" 2>/dev/null || echo 0)
check_zero "V-17-leak-met" "$leak_met"
check_zero "V-17-leak-dbg" "$leak_dbg"

# V-18 (P12 anti-drift): jargao novo NAO vaza para os adaptadores. Conta sobre AGENTS.md e
#   .claude/ e exige 0. Glob defensivo: se rg nao achar arquivos, a soma -> 0 (ok).
leak_adapt=$(rg -c 'feed-up|feed-back|feed-forward|Hattie' AGENTS.md .claude/ 2>/dev/null | awk -F: '{s+=$NF} END{print s+0}')
check_zero "V-18-adapt"  "$leak_adapt"

echo "== $fails fail(s) =="
exit $fails
