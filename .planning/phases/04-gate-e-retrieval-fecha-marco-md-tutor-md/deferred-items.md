# Deferred items -- Phase 04

## Plano 04-04 (tutor.md, wave 2): full gate green deferred to merge gate

O `check-phase4.sh` retorna 7 fail(s) NESTE worktree porque a wave 2 roda em
worktrees paralelos: o plano 03 (`fecha-marco.md`, irmao da wave 2) ainda nao foi
mesclado a esta base (cc2da40 tem apenas planos 01 e 02). Todas as 7 falhas sao
checks DE PROPRIEDADE do `fecha-marco.md`, fora do escopo deste plano:

- V-04 (mastery gate em fecha-marco)
- V-05 (campo Capacidade em fecha-marco)
- V-06 (pergunta de extensao/transferencia em fecha-marco)
- V-10 (fecha-marco escreve a Agenda de retrieval)
- V-11b (exatamente 1 proxima acao em fecha-marco)
- V-12-supp-fch (link SDT em fecha-marco)
- V-13-fch (contrato cross-file: literal em fecha-marco)

Todos os checks de propriedade do plano 04 (`tutor.md`) estao VERDES:
V-01, V-02, V-03, V-11a, V-12-supp-tut, V-12-sdt-anchor, V-13-tut. Os checks de
`reference.md` (V-08, V-09, V-13-ref) e `fundamentos.md` (V-14) e o ANTI-LEAK (V-15)
tambem passam.

Acao: o ORQUESTRADOR roda `check-phase4.sh` no merge gate da wave, apos mesclar
os worktrees dos planos 03 e 04 juntos -- ai V-04..V-13-fch ficam satisfeitos pelas
edicoes do plano 03 e o gate completo fica `== 0 fail(s) ==`. NAO editar
`fecha-marco.md` daqui (propriedade do plano 03) nem `check-phase4.sh` (propriedade
do plano 01).
