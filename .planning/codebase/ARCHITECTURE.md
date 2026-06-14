# ARCHITECTURE — Aprenda Qualquer Coisa

> Padrao de design e fluxo. Este "sistema" e um **toolkit de instrucoes para agentes
> de IA**: a arquitetura e a organizacao do conhecimento (metodo, procedimentos,
> templates) e como os agentes a consomem — nao camadas de software em execucao.

## Padrao central: fonte unica + adaptadores finos

O toolkit e **agnostico de LLM** (`README.md:111-112`). O design segue o padrao
**"single source of truth + thin adapters"**:

```
                    mentor/  (FONTE UNICA — markdown neutro)
                    ┌─────────────────────────────────────┐
                    │ metodo.md  (persona/conduta)         │
                    │ novo-projeto / tutor / fecha-marco / │
                    │ debug / spidr-split  (procedimentos) │
                    │ reference.md  (templates + regras)   │
                    └─────────────────────────────────────┘
                       ▲                  ▲              ▲
            aponta │              aponta │       aponta │
        ┌──────────┴───────┐   ┌─────────┴──────┐  ┌────┴──────────────┐
        │ AGENTS.md        │   │ .claude/       │  │ outro contexto    │
        │ (Codex, Kimi,    │   │ output-style + │  │ (GEMINI.md → copia │
        │  Cursor, ...)    │   │ skills (slash) │  │  ou aponta)       │
        └──────────────────┘   └────────────────┘  └───────────────────┘
```

- **Nenhum adaptador duplica conteudo do metodo.** Cada skill do Claude Code
  (`.claude/skills/*/SKILL.md`) e o output style apenas dizem "leia `mentor/<X>.md`
  e siga". Confirmado em `.claude/skills/tutor/SKILL.md:8-9` e
  `.claude/output-styles/mentor-projeto.md:12-13`.
- **Beneficio arquitetural:** mudar o metodo = editar 1 arquivo em `mentor/`; todos os
  hosts herdam. Portabilidade entre ferramentas sem fork de conteudo.

## Camadas (conceituais)

| Camada | Arquivos | Papel |
|---|---|---|
| **Persona** | `mentor/metodo.md` | Conduta permanente (regra de ouro, gate de curadoria, anti-padroes). Carregada no inicio de toda sessao. |
| **Procedimentos** | `mentor/{novo-projeto,tutor,fecha-marco,debug,spidr-split}.md` | Playbooks por situacao, acionados via roteamento. |
| **Referencia** | `mentor/reference.md` | Templates (CAMINHO, PROGRESSO, APRENDIZADO, aula, scaffold) + regras (granularidade, coesao, sondagem). Puxado sob demanda pelos procedimentos. |
| **Adaptadores** | `AGENTS.md`, `.claude/**` | Pontos de entrada por ferramenta; finos, so apontam. |
| **Ferramenta** | `scripts/roadmap_fetch.py` | Unico codigo executavel; auxilia o bootstrap. |
| **Estado (runtime do aluno)** | `.projetos/<slug>/**` (gitignored) | Dados gerados por sessao; fora do repo do toolkit. |

## Fluxo de dados / controle (roteamento por situacao)

O "data flow" e na verdade **roteamento de intencao**: a situacao do aluno dispara a
leitura de um procedimento. Tabela canonica em `AGENTS.md:16-23`:

| Situacao do aluno | Procedimento acionado |
|---|---|
| Projeto novo (sem `PROGRESSO.md`) | `mentor/novo-projeto.md` |
| Volta a estudar / pede revisao | `mentor/tutor.md` |
| Terminou um marco | `mentor/fecha-marco.md` |
| Travado num erro | `mentor/debug.md` |
| Marco grande/vago demais | `mentor/spidr-split.md` |
| Precisa de template/regra | `mentor/reference.md` |

Convencao transversal: quando qualquer doc cita um `/comando`, significa "leia e siga
`mentor/<comando>.md`" (`AGENTS.md:25-26`).

## Pipeline principal: bootstrap (`mentor/novo-projeto.md`)

O procedimento mais complexo. Ordem **inegociavel** (`mentor/novo-projeto.md:8-11`):

```
diagnostico → sondagem de substrato → caminho completo (Passe 1)
   → montagem de marcos (Passe 2) → APROVACAO (gate) → arquivos
```

Decisao arquitetural-chave: **caminho completo antes dos modulos** (Passe 1 expande
TODOS os passos com dependencias antes de agrupar em marcos no Passe 2). Garante que o
passo N nunca pressupoe conceito nao introduzido (`README.md:135-138`,
`mentor/novo-projeto.md:52-67`). Nenhum arquivo e criado antes da aprovacao do aluno
(regra "Demanda-First", `mentor/novo-projeto.md:83-88`).

## Abstracoes centrais (o "modelo de dominio")

- **Passo** — unidade atomica de ensino (1 conceito dominante novo, ID estavel
  `c0x-slug`). Vive em `CAMINHO.md`.
- **Marco** — fatia vertical de passos consecutivos que entrega algo observavel;
  enquadrado como User Story; vira `git tag marco-NN-<slug>`.
- **Aula** (`aulas/P0x-<slug>.md`) — teoria minima por passo, revelada just-in-time.
- **Scaffold** — esqueleto de codigo com `TODO(human)` (a parte do aluno).
- **Substrato** — nivel medido por sondagem, por assunto (nao por aluno).
- **Walking Skeleton** — marco 00, prova que as camadas conectam sem logica de negocio.

## Pontos de entrada

- **Claude Code:** `/config` -> Output style -> `mentor-projeto`; depois skills slash.
- **Codex/Kimi/Cursor:** abrir a ferramenta dentro do repo (le `AGENTS.md`
  automaticamente); interacao em linguagem natural (`README.md:71-86`).
- **Codigo:** `scripts/roadmap_fetch.py` via `python ... main()`
  (`scripts/roadmap_fetch.py:142-168`).
