# STRUCTURE — Aprenda Qualquer Coisa

> Layout de diretorios, locais-chave e convencoes de nomes. 18 arquivos versionados
> (15 markdown, 1 Python, 2 config). Repositorio pequeno e plano.

## Arvore de diretorios (versionado)

```
aprenda-qualquer-coisa/
├── AGENTS.md                       # entrada universal (Codex/Kimi/Cursor) — roteia situacoes
├── README.md                       # doc para leigos + "como funciona por dentro"
├── aprenda-qualquer-coisa.code-workspace   # workspace VS Code (49B)
├── .gitignore                      # ignora CLAUDE.md e .projetos/
│
├── mentor/                         # METODO — fonte unica, markdown neutro (agnostico de LLM)
│   ├── metodo.md                   # persona/conduta permanente (165 linhas)
│   ├── novo-projeto.md             # bootstrap: diagnostico→sondagem→caminho→marcos→arquivos
│   ├── tutor.md                    # copiloto de sessao
│   ├── fecha-marco.md              # fechamento de marco (done→curadoria→tag→recalibra)
│   ├── debug.md                    # protocolo de forense (6 passos)
│   ├── spidr-split.md              # decomposicao de marcos (5 eixos SPIDR)
│   └── reference.md                # templates + regras (maior arquivo: 419 linhas)
│
├── .claude/                        # adaptadores Claude Code (apontam para mentor/)
│   ├── settings.local.json         # config local da maquina (nao e metodo)
│   ├── output-styles/
│   │   └── mentor-projeto.md        # persona; ativa via /config → Output style
│   └── skills/                     # skills slash, finas (frontmatter + "leia mentor/X.md")
│       ├── novo-projeto/SKILL.md
│       ├── tutor/SKILL.md
│       ├── fecha-marco/SKILL.md
│       ├── debug/SKILL.md
│       └── spidr-split/SKILL.md
│
└── scripts/
    └── roadmap_fetch.py            # baixa roadmaps de roadmap.sh (stdlib, opcional)
```

## Diretorios ignorados (existem em runtime, nao versionados)

Definidos em `.gitignore`:

- **`CLAUDE.md`** — instrucoes locais do Claude Code, fora do metodo portatil.
- **`.projetos/`** — **a casa dos projetos do aluno.** Cada `.projetos/<slug>/` e um
  projeto de aprendizado e seu **proprio repo git** independente. Pessoal por design:
  nao sobe pro github do toolkit (`AGENTS.md:29-34`, `mentor/reference.md:167-184`).

### Layout de um projeto do aluno (`.projetos/<slug>/`, gerado pelo bootstrap)

Documentado em `mentor/reference.md:173-184`:

```
.projetos/<slug>/
├── CAMINHO.md            # design: passos detalhados + mapa passos→marcos
├── PROGRESSO.md          # acompanhamento: substrato, DoD, marcos, dividas, log
├── APRENDIZADO.md        # diario: licoes, padroes de erro, decisoes
├── referencias/          # roadmaps de referencia (saida de roadmap_fetch.py)
├── aulas/                # teoria minima POR PASSO (P0x-<slug>.md), lida antes do scaffold
├── exercicios/           # drills ISOLADOS, just-in-time (pasta-por-conceito so aqui)
└── projeto/              # o ARTEFATO UNICO; cresce marco a marco (marcos = git tags)
```

## Locais-chave (onde encontrar o que)

| Procurando... | Va para |
|---|---|
| Regra de ouro, anti-padroes, ciclo por marco | `mentor/metodo.md` |
| Todos os templates (CAMINHO, PROGRESSO, aula, scaffold) | `mentor/reference.md` |
| Como o bootstrap funciona | `mentor/novo-projeto.md` |
| Roteamento de situacao → procedimento | `AGENTS.md:16-23` |
| Como ativar a persona no Claude Code | `README.md:32-48` |
| Unico codigo executavel | `scripts/roadmap_fetch.py` |
| Onde mora o estado do aluno | `.projetos/<slug>/` (gitignored) |

## Convencoes de nomes

- **Procedimentos:** um arquivo por situacao em `mentor/`, nome = nome do comando
  (`tutor.md` ↔ `/tutor`). Convencao explicita em `AGENTS.md:25-26`.
- **Skills Claude Code:** `.claude/skills/<comando>/SKILL.md` (pasta por skill,
  frontmatter `name`/`description`).
- **IDs de conceito:** `c0x-<slug>` estaveis (ex: `c01-tags-html`) — `mentor/reference.md:88`.
- **Passos:** `P0x` (ex: `P01`, `P02`) — `mentor/reference.md:64`.
- **Aulas:** `aulas/P0x-<slug>.md` (nomeada pelo ID do passo) — `mentor/reference.md:320`.
- **Tags de marco:** `marco-NN-<slug>` no repo do projeto — `mentor/reference.md:158`.
- **Slugs de projeto:** kebab-case curto — `mentor/novo-projeto.md:93`.
- **Idioma:** todo o conteudo em **portugues** (sem acentos em varios arquivos, por
  escolha de robustez de encoding entre ferramentas).
