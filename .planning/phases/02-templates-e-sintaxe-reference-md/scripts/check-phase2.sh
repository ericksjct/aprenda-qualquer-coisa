#!/usr/bin/env sh
# check-phase2.sh -- smoke-test estatico (gate da Fase 2).
#
# Roda os comandos rg da tabela "Per-Task Verification Map" (02-VALIDATION.md) contra
# mentor/reference.md e mentor/fundamentos.md, imprime PASS/FAIL por criterio e retorna
# exit != 0 se qualquer checagem falhar.
#
# Duas familias de checagem:
#   - check_min  LABEL  COUNT  MIN   -> PASS quando COUNT >= MIN (criterios positivos)
#   - check_zero LABEL  COUNT         -> PASS quando COUNT == 0  (so o anti-leak CONS-01)
#
# Nota sobre o baseline: no estado ATUAL de reference.md (antes das edicoes dos planos
# 02 e 03) varias checagens POSITIVAS vao FALHAR -- isso e esperado e correto. O script so
# fica todo-verde apos as edicoes. A unica checagem que ja deve passar hoje e ANTI-LEAK
# (baseline 0). Este script e o gate: re-rode-o a cada commit que toca um bloco cercado.

DIR=$(dirname "$0")
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

echo "== Phase 2 static smoke-test =="

# 1. EST-01a: linha "Objetivo (capacidade):" no bloco CAMINHO
check_min "EST-01a" "$(count 'Objetivo \(capacidade\):' "$REF")" 1

# 2. EST-01b: cabecalho "## Objetivo do passo"
check_min "EST-01b" "$(count '^## Objetivo do passo' "$REF")" 1

# 3. EST-04: "nos fazemos" no titulo + corpo (>= 2)
check_min "EST-04" "$(count 'nos fazemos' "$REF")" 2

# 4. EST-02: pelo menos 2 links para fundamentos.md#
check_min "EST-02" "$(count '\]\(fundamentos\.md#' "$REF")" 2

# 5. CARGA-01: fading/expertise-reversal na secao de substrato
check_min "CARGA-01" "$(count 'expertise-reversal|suporte demais|recua' "$REF")" 1

# 6. CARGA-02: worked example analogo (instancia diferente)
check_min "CARGA-02" "$(count 'instancia diferente|exemplo resolvido' "$REF")" 1

# 7. CARGA-03: limite honesto de Mayer (3 de 12)
check_min "CARGA-03" "$(count '3 de 12' "$REF")" 1

# 8. ANCHOR-RESOLVE: as 2 ancoras esperadas existem como heading em fundamentos.md
if rg -q '^## Frameworks foundational \(load-bearing\)' "$FUN" 2>/dev/null && \
   rg -q '^### Mayer: so 3 de 12 principios em texto puro' "$FUN" 2>/dev/null; then
  printf 'PASS  %-16s ambas as ancoras resolvem em %s\n' "ANCHOR-RESOLVE" "$FUN"
else
  printf 'FAIL  %-16s ancora ausente em %s\n' "ANCHOR-RESOLVE" "$FUN"
  fails=$((fails + 1))
fi

# 9. ANTI-LEAK (CONS-01): NENHUM jargao de framework DENTRO de bloco cercado -> deve ser 0.
#    Esta e a UNICA checagem negativa (= 0); as demais sao positivas (>= N).
LEAK_PAT='Bloom|backward design|GRR|Mayer|expertise-reversal|constructive alignment|cognitive load'
leak=$(sh "$DIR/extract-fenced.sh" "$REF" | rg -c "$LEAK_PAT" 2>/dev/null || echo 0)
check_zero "ANTI-LEAK" "$leak"

echo "== $fails fail(s) =="
exit $fails
