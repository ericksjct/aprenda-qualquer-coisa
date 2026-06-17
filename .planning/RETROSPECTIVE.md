# Retrospective — Mentor de Aprendizado por Projeto

Living retrospective. One section per milestone; cross-milestone trends at the end.

## Milestone: v1.0 — Ancoragem em ciencia da aprendizagem

**Shipped:** 2026-06-17
**Phases:** 6 | **Plans:** 16 | **Tasks:** 24 | **Requirements:** 21/21

### What Was Built

O metodo do toolkit passou de caseiro a ancorado em ciencia da aprendizagem reconhecida.
`mentor/fundamentos.md` virou o catalogo interno upstream (6+6 frameworks com fonte, termo do
metodo e "aplicado em <doc>"); `reference.md` ganhou verbo de capacidade, GRR de 3 fases, worked
example e Mayer; `novo-projeto.md` ganhou Stage 2 + primeiro done leve; `fecha-marco.md`/`tutor.md`
viraram mastery gate + retrieval ativo + revisao espacada; `metodo.md`/`debug.md` fixaram
anti-theory-leak + feedback tri-partido de Hattie. A Fase 6 entregou `check-consistencia.sh`, o
primeiro tool de verificacao mecanica permanente.

### What Worked

- **Ordem de build fonte-unica inegociavel** (fundamentos -> reference -> ... -> auditoria):
  evitou drift semantico; cada doc downstream consumia vocabulario ja fixado upstream.
- **Verificacao mecanica por fase** (harness `check-phaseN.sh` + extract-fenced): cada fase
  fechou com gate verde por grep, nao por julgamento. A auditoria de marco foi quase trivial
  porque a prova ja estava codificada.
- **Anti-cargo-cult por construcao:** exigir "aplicado em <doc>" verificavel para cada teoria
  impediu teoria orfa.

### What Was Inefficient

- **Bookkeeping de requisitos atrasou a realidade:** REQUIREMENTS.md ficou em 7/21 [x] mesmo com
  tudo entregue; o SUMMARY frontmatter do 02-03 nao registrou 5 reqs. A entrega estava certa
  (VERIFICATION.md autoritativa), mas o placar mentia — exigiu reconciliacao no fechamento.
- **Artefato de tool-call vazou para um PLAN.md** (`</content></invoke>` em 06-01) — pego e
  limpo no preflight do fechamento.
- **Nyquist wave-0 ficou parcial** em 4 de 6 fases (gates mecanicos verdes, mas o ritual de
  validacao nao foi completado).

### Patterns Established

- Harness de verificacao por fase como gate obrigatorio (clonado byte-a-byte entre fases).
- "Aplicado em <doc>" como contrato verificavel de toda teoria adicionada.
- mentor/ sem acentos; paths em backticks; teoria single-sourced (so prosa, nunca em bloco
  cercado de artefato do aluno) para nao vazar jargao ao aluno.

### Key Lessons

- Atualizar o checkbox/frontmatter de requisito na MESMA entrega que o satisfaz — senao o placar
  diverge e o fechamento vira arqueologia.
- A auditoria de marco com cruzamento de 3 fontes (VERIFICATION + SUMMARY + traceability) pega
  exatamente esse tipo de divergencia de bookkeeping antes de selar.

### Cost Observations

- Model mix: predominantemente opus (perfil `quality`).
- Notable: o investimento em harness mecanico por fase pagou no fechamento — auditoria rapida,
  zero re-verificacao manual.

---

## Cross-Milestone Trends

| Milestone | Phases | Plans | Requirements | Shipped |
|-----------|--------|-------|--------------|---------|
| v1.0 Ancoragem em ciencia da aprendizagem | 6 | 16 | 21/21 | 2026-06-17 |

_Trends a acumular a partir do v2.0._
