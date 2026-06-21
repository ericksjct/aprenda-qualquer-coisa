# Phase 7: Ingestao de PDF do livro via docling - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-21
**Phase:** 07-ingestao-pdf-livro-via-docling
**Areas discussed:** Integracao no metodo, Politica de dependencia / setup, Forma da conversao (output), Invocacao / quem roda

---

## Integracao no metodo

### Papel do markdown convertido
| Option | Description | Selected |
|--------|-------------|----------|
| Fonte pro CAMINHO | Mentor le o livro pra extrair conceitos/ordem; livro vira espinha do curso | |
| Material de consulta | Acervo consultavel, nao dirige o CAMINHO | |
| Ambos / em camadas | Alimenta o CAMINHO e fica como consulta | |

**User's choice:** (free text) Livro = guideline/baseline. A pesquisa do mentor pode divergir da literatura do aluno; em divergencia o mentor ou (1) sinaliza fonte outdated e mostra jeito melhor, ou (2) adota a convencao do livro como embasamento teorico.
**Notes:** Resposta mais rica que as opcoes — virou D-01 + protocolo de divergencia (D-03/D-04).

### Encaixe no fluxo
| Option | Description | Selected |
|--------|-------------|----------|
| Passo no bootstrap | Passo opcional em novo-projeto.md | ✓ |
| Ferramenta avulsa | So script + doc, como roadmap_fetch.py | |
| Voce decide | Criterio do agente | |

**User's choice:** Passo no bootstrap

### Quem decide na divergencia livro vs pratica
| Option | Description | Selected |
|--------|-------------|----------|
| Mentor julga, aluno confirma | Mentor explica e recomenda; aluno decide | |
| Aluno define a politica no inicio | Aluno escolhe priorizar livro ou pratica de antemao | |
| Mentor decide sozinho | Criterio proprio (recencia/consenso), so registra | ✓ |

**User's choice:** Mentor decide sozinho
**Notes:** Tensiona a regra de ouro; mitigado por registro datado em APRENDIZADO.md.

### Onde registra a divergencia
| Option | Description | Selected |
|--------|-------------|----------|
| APRENDIZADO.md | Diario de licoes/decisoes existente; entrada datada | ✓ |
| Bloco no livro convertido | Callout inline no markdown | |
| Voce decide | Criterio do agente | |

**User's choice:** APRENDIZADO.md

---

## Politica de dependencia / setup

### Tratamento da dep docling
| Option | Description | Selected |
|--------|-------------|----------|
| Opcional com fallback | Dep opcional isolada; core segue sem | ✓ |
| Dep de primeira classe | requirements/pyproject, setup esperado | |
| Servico/CLI externo | docling rodado por fora, script so consome | |

**User's choice:** (refinado) Opcional com fallback — E se o aluno ja tem o livro em .md, ele cola na pasta sem passar pelo docling. O script docling e ferramenta opcional.
**Notes:** Refinamento-chave (D-06): contrato do metodo = markdown em livro/, nao docling.

### Isolamento da dependencia
| Option | Description | Selected |
|--------|-------------|----------|
| requirements opcional + venv | Arquivo de deps so pro script; core intocado | ✓ |
| Check em runtime | Import try/except com mensagem de instalacao | |
| Voce decide | Criterio do agente | |

**User's choice:** requirements opcional + venv

---

## Forma da conversao (output)

### Pasta do markdown do livro
| Option | Description | Selected |
|--------|-------------|----------|
| livro/ (nova) | Pasta dedicada .projetos/<slug>/livro/ | ✓ |
| referencias/ | Reusa pasta do roadmap_fetch.py | |
| Voce decide | Criterio do agente | |

**User's choice:** livro/ (nova)

### Estrutura do markdown
| Option | Description | Selected |
|--------|-------------|----------|
| Split por capitulo/secao | Quebra por headings detectados | ✓ |
| Arquivo unico | Tudo num .md so | |
| Voce decide | Criterio do agente | |

**User's choice:** (com nota) Split por capitulo/secao, MAS maximizar scripts deterministicos pra tirar responsabilidade da LLM. Aproveitar script pronto em C:\Users\Erick\Documents\Projetos\docling-extrair-pdf\converter.py (funciona, so nao faz split). Importante: tutor saber a PAGINA do livro pra referenciar ao aluno (aprendizado multi-midia).
**Notes:** Gerou D-09 (split deterministico), D-10 (ancora de pagina) e a canonical ref do converter.py.

### Fidelidade
| Option | Description | Selected |
|--------|-------------|----------|
| Estrutura > tabelas/figuras | Headings/ordem primeiro; resto best-effort | ✓ |
| Alta fidelidade | Preservar tabelas/formulas/figuras | |
| Voce decide | Criterio do agente | |

**User's choice:** Estrutura > tabelas/figuras

---

## Invocacao / quem roda

### Quem roda a conversao
| Option | Description | Selected |
|--------|-------------|----------|
| Aluno roda, CLI por args | Adapta script p/ CLI; aluno roda | |
| Agente dispara via skill | Skill /comando, agente chama por Bash | ✓ (+ aluno tambem) |
| Mantem questionary | Menu interativo preservado | |

**User's choice:** (free text) Agente pode disparar via skill, mas o aluno tambem pode. Se o agente disparar: avisar ANTES que vai levar tempo, nao consome tokens (roda local), e mostrar o progresso do script.
**Notes:** Gerou D-13/D-14. Combinado com D-12 (remover questionary, virar CLI por args).

### Como o bootstrap dirige
| Option | Description | Selected |
|--------|-------------|----------|
| Pergunta + instrucao | Mentor pergunta 'tem livro? PDF ou .md?' e instrui | ✓ |
| So consome se existir | Nao pergunta; usa livro/ se ja existir | |
| Voce decide | Criterio do agente | |

**User's choice:** Pergunta + instrucao

---

## Claude's Discretion

- Nome exato da skill e do script; formato exato da ancora de pagina; nome do requirements
  opcional; criterio de corte do split (H1 vs H2); tratamento de livro em idioma diferente.

## Deferred Ideas

- Alta-fidelidade de tabelas/formulas/figuras (best-effort agora).
- i18n do toolkit (outro item do v2.0).
- Atualizar PROJECT.md: mover "codigo de aplicacao / runtime novo" de Out of Scope para Validated.
