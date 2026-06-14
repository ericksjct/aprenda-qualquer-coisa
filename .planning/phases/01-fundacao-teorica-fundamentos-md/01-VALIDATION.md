---
phase: 1
slug: fundacao-teorica-fundamentos-md
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-06-14
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.
> **Nota:** esta e uma fase de AUTORIA DE DOC (markdown interno). Nao ha codigo,
> framework de teste, nem comando de teste. A "validacao" e revisao do doc contra os
> criterios — muitos checks sao automatizaveis via `grep`/`ls` (existencia de secoes,
> paths, strings). Os checks de qualidade redacional (nao inflar, def 1-linha) sao manuais.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Nenhum (doc-authoring) — verificacao por `grep`/`ls` + revisao manual |
| **Config file** | none — N/A |
| **Quick run command** | `grep`/`ls` contra `mentor/fundamentos.md` (ver Per-Task Map) |
| **Full suite command** | Checklist de aceite completo (ver baixo) |
| **Estimated runtime** | ~5 s (greps) + revisao manual |

---

## Sampling Rate

- **After every task commit:** Rodar os `grep`/`ls` da entrada/secao tocada.
- **After every plan wave:** Rodar o checklist de aceite completo.
- **Before `/gsd-verify-work`:** Checklist completo verde + revisao manual dos itens de qualidade.
- **Max feedback latency:** ~10 s para os checks automatizaveis.

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 1-01-01 | 01 | 1 | FUND-03 | — | N/A | grep | `grep -i "interno" mentor/fundamentos.md` (preambulo de uso interno) | ❌ W0 | ⬜ pending |
| 1-01-02 | 01 | 1 | FUND-01 | — | N/A | grep | `grep -c "Fonte primaria\|aplicado em" mentor/fundamentos.md` (12 entradas, 4 campos) | ❌ W0 | ⬜ pending |
| 1-01-03 | 01 | 1 | FUND-01 | — | N/A | ls | `ls mentor/` — cada doc citado em "aplicado em" existe | ❌ W0 | ⬜ pending |
| 1-01-04 | 01 | 1 | Criterio #4 | — | N/A | grep | `grep -i "Mayer\|relatedness\|SDT" mentor/fundamentos.md` (ressalvas) | ❌ W0 | ⬜ pending |
| 1-01-05 | 01 | 1 | FUND-02 | — | N/A | grep | `grep -i "NAO usamos\|estilos de aprendizagem\|Cone de Dale" mentor/fundamentos.md` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*
*File Exists = ❌ W0: o arquivo `mentor/fundamentos.md` so passa a existir durante a Wave 1 (e o entregavel da fase).*

---

## Wave 0 Requirements

*None — fase de autoria, sem infraestrutura de teste a montar. A verificacao e a revisao
do doc pelo checklist de aceite abaixo. `mentor/fundamentos.md` ainda nao existe ate a Wave 1.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Cada definicao tem EXATAMENTE 1 linha (anti-paredao) | FUND-01 | Qualidade redacional nao e grep-avel de forma confiavel | Ler cada entrada; nenhuma definicao com >1 linha; mini-notas curtas (1-2 frases) |
| Ressalvas SDT/Mayer "sem inflar os claims" | Criterio #4 | Tom/exatidao do claim e julgamento editorial | Conferir: relatedness fraca em solo+IA (ancorar em autonomia+competencia); Mayer so coerencia/sinalizacao/segmentacao |
| "termo no metodo" nao inventa jargao novo | FUND-01 | Exige cruzar com vocabulario real dos `mentor/*.md` | Cada termo aparece em algum `mentor/*.md` existente |
| Status de "aplicado em" coerente com build order | CONS-02 (prep) | Requer entender a ordem das Fases 2-6 | `(Fase N, pendente)` para destinos futuros; `(ja presente)` so onde a aplicacao ja existe hoje |

---

## Validation Sign-Off

- [ ] Todos os checks automatizaveis (`grep`/`ls`) verdes
- [ ] Sampling continuity: cada requisito (FUND-01/02/03, Criterio #4, CONS-02) tem ao menos um check
- [ ] Wave 0 N/A (sem infraestrutura) — confirmado
- [ ] Sem watch-mode flags (N/A)
- [ ] Feedback latency < 10s (greps)
- [ ] Itens manuais (qualidade redacional) revisados
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
