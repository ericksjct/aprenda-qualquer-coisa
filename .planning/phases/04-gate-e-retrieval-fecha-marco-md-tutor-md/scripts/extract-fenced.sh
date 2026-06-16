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
