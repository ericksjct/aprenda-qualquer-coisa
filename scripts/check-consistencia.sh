#!/usr/bin/env sh
# check-consistencia.sh -- auditoria de consistencia permanente (CONS-02 + CONS-03 + IN-01).
# Roda da RAIZ do repo. Imprime PASS/FAIL por criterio; exit = numero de falhas (0 = verde).
# Pre-requisito: ripgrep (rg). Codifica V-01..V-16 do contrato Nyquist (06-VALIDATION.md).
# Helpers clonados do padrao de harness das Fases 2/4/5 (check-phaseN.sh).

command -v rg >/dev/null 2>&1 || { echo "check-consistencia.sh: requer ripgrep (rg)"; exit 2; }

fails=0

check_min()  { l="$1"; v="$2"; m="$3"; [ "$v" -ge "$m" ] && printf 'PASS  %-22s %s>=%s\n' "$l" "$v" "$m" || { printf 'FAIL  %-22s %s>=%s\n' "$l" "$v" "$m"; fails=$((fails+1)); }; }
check_zero() { l="$1"; v="$2"; [ "$v" -eq 0 ] && printf 'PASS  %-22s =0\n' "$l" || { printf 'FAIL  %-22s got=%s need=0\n' "$l" "$v"; fails=$((fails+1)); }; }
check_has()  { l="$1"; p="$2"; f="$3"; rg -q "$p" "$f" 2>/dev/null && printf 'PASS  %-22s in %s\n' "$l" "$f" || { printf 'FAIL  %-22s NOT in %s\n' "$l" "$f"; fails=$((fails+1)); }; }

echo "== CONS-02: anti-cargo-cult (cada teoria de fundamentos.md aterrissa no doc citado) =="
check_has "C2-backward-ref"   'backward design'                 mentor/reference.md
check_has "C2-backward-novo"  'backward design'                 mentor/novo-projeto.md
check_has "C2-align"          'Objetivo \(capacidade\)'         mentor/reference.md
check_has "C2-mayer"          'so 3 de 12 principios|coerencia' mentor/reference.md
check_has "C2-expertrev"      'expertise-reversal'              mentor/reference.md
check_has "C2-retrieval"      'retrieval practice'              mentor/tutor.md
check_has "C2-sdt"            'proxima acao'                    mentor/tutor.md
check_has "C2-mastery"        'mastery learning'                mentor/fecha-marco.md
check_has "C2-formativa"      'auto-explicacao'                 mentor/metodo.md
check_has "C2-hattie"         'feed-forward'                    mentor/debug.md
check_has "C2-spacing"        'Agenda de retrieval'             mentor/fecha-marco.md

echo "== CONS-03 #1 (V-12): cada /comando tem mentor/<comando>.md (set fechado) =="
for cmd in novo-projeto tutor fecha-marco debug spidr-split; do
  [ -f "mentor/$cmd.md" ] && printf 'PASS  cmd-%-18s mentor/%s.md\n' "$cmd" "$cmd" \
    || { printf 'FAIL  cmd-%-18s MISSING mentor/%s.md\n' "$cmd" "$cmd"; fails=$((fails+1)); }
done

echo "== CONS-03 #2 (V-13): paths em backticks resolvem (com SKIP de not-in-repo) =="
SKIP='(<slug>|<comando>|<conceito>|P0x|GEMINI\.md|CAMINHO\.md|PROGRESSO\.md|APRENDIZADO\.md|aulas/|exercicios/|projeto/|referencias/|^reference\.md$|^metodo\.md$)'
unresolved=$(rg -oN '`[A-Za-z0-9_./<>-]+\.(md|py|sh|json)`' mentor/ AGENTS.md README.md \
  | sed 's/.*`\(.*\)`/\1/' | sort -u \
  | while IFS= read -r p; do echo "$p" | rg -q "$SKIP" && continue; [ -f "$p" ] || echo "$p"; done | wc -l | tr -d ' ')
check_zero "backtick-paths" "$unresolved"

echo "== CONS-03 #3 (V-14): zero jargao de metodo nos adaptadores (AGENTS.md + .claude/) =="
LEAK='SDT|mastery|spacing|backward design|Bloom|GRR|Mayer|retrieval practice|testing effect|feed-up|feed-back|feed-forward|Hattie|expertise-reversal|cognitive load|constructive alignment|formativ'
leak=$(rg -c "$LEAK" AGENTS.md .claude/ 2>/dev/null | awk -F: '{s+=$NF} END{print s+0}')
check_zero "adapter-jargon" "$leak"

echo "== CONS-03 set-equality (V-15): conjunto de procedimentos -- DOIS LADOS por arquivo =="
# Fonte canonica do conjunto (D-06): tabela de roteamento de AGENTS.md.
# Igualdade de CONJUNTO "sem sobra nem falta" sobre AGENTS.md, README.md e mentor/metodo.md.
CANON='novo-projeto tutor fecha-marco debug spidr-split'
# Nao-comandos conhecidos que aparecem como `/x` mas NAO sao procedimentos do mentor:
#   /config e /clear sao app-commands do Claude Code; /comando e o placeholder literal da convencao.
# converte-livro: comando real que roteia para mentor/novo-projeto.md (passo livro-base);
#   NAO tem mentor/converte-livro.md proprio (excecao documentada a convencao /comando).
NONCMD='novo-projeto|tutor|fecha-marco|debug|spidr-split|converte-livro|config|clear|comando'
for f in AGENTS.md README.md mentor/metodo.md; do
  # LADO POSITIVO: os 5 comandos canonicos aparecem no arquivo (falta de qualquer um -> FAIL).
  missing=0
  for cmd in $CANON; do rg -q "$cmd" "$f" 2>/dev/null || missing=$((missing+1)); done
  # LADO NEGATIVO (anti-drift): nenhum `/comando` FORA do set de 5 (excluidos os nao-comandos).
  # Extrai tokens `/nome` delimitados por backtick (`/x`) -- nunca componentes de path como mentor/metodo.md.
  extra=$(rg -oN '`/[a-z][a-z-]+`' "$f" 2>/dev/null | tr -d '`' | sed 's,^/,,' | sort -u \
    | rg -vc "^($NONCMD)$" 2>/dev/null || echo 0)
  if [ "$missing" -eq 0 ] && [ "$extra" -eq 0 ]; then
    printf 'PASS  set-eq %-15s 5 canonicos presentes, 0 fora-do-set\n' "$f"
  else
    printf 'FAIL  set-eq %-15s faltando=%s fora-do-set=%s\n' "$f" "$missing" "$extra"; fails=$((fails+1))
  fi
done

echo "== IN-01 (V-16): zero letras acentuadas nos docs de conduta (mentor/ exceto reference.md) =="
# Docs de conduta do agente sao ASCII (robustez de encoding). reference.md e excluido:
# ele guarda os TEMPLATES de artefato do aluno, que por regra usam portugues acentuado
# (ver "Idioma e acentuacao" em mentor/reference.md). Artefatos vivem em .projetos/ (gitignored).
acc=$(rg -c '[áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ]' mentor/ -g '!reference.md' 2>/dev/null | awk -F: '{s+=$NF} END{print s+0}')
check_zero "accents-conduta" "$acc"

echo "== $fails fail(s) =="
exit $fails
