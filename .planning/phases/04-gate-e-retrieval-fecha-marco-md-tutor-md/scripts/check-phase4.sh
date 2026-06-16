#!/usr/bin/env sh
# check-phase4.sh -- smoke-test estatico (gate da Fase 4).
#
# Roda os comandos rg da tabela "Per-Task Verification Map" (04-VALIDATION.md) contra
# mentor/tutor.md, mentor/fecha-marco.md, mentor/reference.md e mentor/fundamentos.md,
# imprime PASS/FAIL por criterio e retorna exit != 0 se qualquer checagem falhar.
#
# Tres familias de checagem (clonadas verbatim de check-phase2.sh):
#   - check_min  LABEL  COUNT  MIN   -> PASS quando COUNT >= MIN (criterios positivos)
#   - check_zero LABEL  COUNT         -> PASS quando COUNT == 0  (so o anti-leak CONS-01)
#   - check_has  LABEL  PAT   FILE    -> PASS quando rg -q acha o padrao (ANCHOR/CONTRACT)
#
# Nota sobre o baseline: ANTES das edicoes dos planos 02/03/04, varias checagens POSITIVAS
# vao FALHAR -- isso e esperado e correto, mesma convencao da Fase 2. So V-14 (ANCHOR-RESOLVE,
# as 3 headings ja existem em fundamentos.md) e V-15 (ANTI-LEAK, baseline 0) passam no baseline.
# Este script e o gate FINAL desde o Wave 0 -- nenhum plano posterior edita este arquivo.

DIR=$(dirname "$0")
TUT="mentor/tutor.md"
FCH="mentor/fecha-marco.md"
REF="mentor/reference.md"
FUN="mentor/fundamentos.md"
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

echo "== Phase 4 static smoke-test =="

# V-01 (AVAL-01): heading de recuperacao ativa presente no tutor
check_min "V-01" "$(count '[Rr]ecuperacao ativa' "$TUT")" 1

# V-02 (AVAL-01/D-02): tutor referencia a Agenda de retrieval
check_min "V-02" "$(count 'Agenda de retrieval' "$TUT")" 1

# V-03 (AVAL-01/D-04): regra skip-on-empty (case-robusto via classes de char, sem -i)
check_min "V-03" "$(count '[Aa]genda.*vazia|[Nn]enhum conceito|[Pp]ule|[Ss]em entrada' "$TUT")" 1

# V-04 (AVAL-03): Passo 1 reframed como mastery gate
check_min "V-04" "$(count 'mastery gate|gate de maestria|gate de marco' "$FCH")" 1

# V-05 (AVAL-03/D-06): gate le o campo Capacidade
check_min "V-05" "$(count 'Capacidade' "$FCH")" 1

# V-06 (AVAL-04/D-07): pergunta de extensao/transferencia presente
check_min "V-06" "$(count 'como voce mudaria|estender|extensao|transferencia' "$FCH")" 1

# V-07 (AVAL-04/D-08): blocking-formative -- marco NAO fecha na falha
check_min "V-07" "$(count 'NAO .*fecha|volte ao ciclo' "$FCH")" 1

# V-08 (AVAL-02): secao ## Agenda de retrieval no template PROGRESSO
check_min "V-08" "$(count '## Agenda de retrieval' "$REF")" 1

# V-09 (AVAL-02/D-09): secao ## Dividas de aprendizado distinta (coexiste com V-08)
check_min "V-09" "$(count '## Dividas de aprendizado' "$REF")" 1

# V-10 (AVAL-02): fecha-marco escreve a entrada da Agenda de retrieval
check_min "V-10" "$(count 'Agenda de retrieval' "$FCH")" 1

# V-11 (ENG-01): "exatamente 1 proxima acao" no tutor (a) E no fecha-marco (b)
check_min "V-11a" "$(count 'exatamente 1|uma .*proxima acao|1 proxima acao' "$TUT")" 1
check_min "V-11b" "$(count 'exatamente 1|uma .*proxima acao|1 proxima acao' "$FCH")" 1

# V-12 (ENG-01/D-13): link SDT em prosa nos dois arquivos
check_min "V-12-supp-tut" "$(count 'fundamentos\.md#frameworks-supporting-ancoram-um-doc' "$TUT")" 1
check_min "V-12-supp-fch" "$(count 'fundamentos\.md#frameworks-supporting-ancoram-um-doc' "$FCH")" 1
v12_sdt=$(( $(count 'fundamentos\.md#sdt-relatedness-em-solo-ia' "$TUT") + $(count 'fundamentos\.md#sdt-relatedness-em-solo-ia' "$FCH") ))
check_min "V-12-sdt-anchor" "$v12_sdt" 1

# V-13 (CONTRACT cross-file): literal "Agenda de retrieval" nos 3 arquivos
check_has "V-13-ref" "Agenda de retrieval" "$REF"
check_has "V-13-fch" "Agenda de retrieval" "$FCH"
check_has "V-13-tut" "Agenda de retrieval" "$TUT"

# V-14 (ANCHOR-RESOLVE): as 3 ancoras usadas resolvem como heading em fundamentos.md
if rg -q '^## Frameworks supporting \(ancoram um doc\)' "$FUN" 2>/dev/null && \
   rg -q '^### SDT relatedness em solo' "$FUN" 2>/dev/null && \
   rg -q '^## Frameworks foundational \(load-bearing\)' "$FUN" 2>/dev/null; then
  printf 'PASS  %-16s as 3 ancoras resolvem em %s\n' "V-14" "$FUN"
else
  printf 'FAIL  %-16s ancora ausente em %s\n' "V-14" "$FUN"
  fails=$((fails + 1))
fi

# V-15 (CONS-01 anti-leak): NENHUM jargao de framework DENTRO de bloco cercado -> deve ser 0.
#   Padrao CANONICO FINAL: forma de FRASE para retrieval ("retrieval practice|testing effect")
#   -- mantem a cobertura anti-leak de teoria de recuperacao SEM falso-positivo no rotulo de
#   contrato legitimo "## Agenda de retrieval". O token isolado "retrieval" NAO entra no padrao.
LEAK_PAT='SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect'
leak=$(sh "$DIR/extract-fenced.sh" "$REF" | rg -c "$LEAK_PAT" 2>/dev/null || echo 0)
check_zero "ANTI-LEAK" "$leak"

echo "== $fails fail(s) =="
exit $fails
