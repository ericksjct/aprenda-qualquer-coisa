# Aprenda Qualquer Coisa · Learn Anything

> Toolkit de **mentoria de aprendizado por projeto** para o [Claude Code](https://code.claude.com).
> A project-based learning **mentor toolkit** for [Claude Code](https://code.claude.com).

Em vez de o agente escrever o código por você, ele **conduz você a escrevê-lo**: desenha a
estrutura, deixa marcadores `TODO(human)`, faz perguntas socráticas e só sugere melhorias
**depois que o código funciona**. O projeto é o laboratório; o objetivo é você conseguir
explicar e estender o que construiu sozinho.

_Instead of the agent writing the code for you, it **guides you to write it**: it designs
the structure, leaves `TODO(human)` markers, asks socratic questions, and only suggests
improvements **after the code works**. The project is the lab; the goal is for you to be
able to explain and extend what you built on your own._

---

## 🇧🇷 Português

### O que tem aqui

Dois componentes que se dividem responsabilidades:

| Componente | Arquivo | Papel |
|---|---|---|
| **Output style** (persona) | `.claude/output-styles/mentor-projeto.md` | Comportamento persistente da sessão — conduta marco a marco. |
| **Skill** (bootstrap) | `.claude/skills/novo-projeto/` | Procedimento invocável uma vez: demanda → roadmap → esqueleto. |

A skill puxa `reference.md` sob demanda (granularidade, templates, layout), mantendo o
`SKILL.md` enxuto.

### Como usar

1. Abra o Claude Code **dentro deste repositório** (os arquivos têm escopo local em `.claude/`).
2. Ative a persona:
   ```
   /output-style mentor-projeto
   ```
3. Faça o bootstrap do seu projeto de aprendizado e descreva no chat o que quer construir
   (anexe um arquivo de referência, ex.: um PDF de design-alvo, se tiver):
   ```
   /novo-projeto
   ```

### Princípios

- **Make it work → make it right → make it fast.** Best-practice antes de funcionar é ruído.
- **Marcos verticais, nunca temas.** Cada marco entrega algo que roda/renderiza.
- **Drill condicional, just-in-time.** Exercício isolado só quando o conceito é novo,
  não-trivial e acima do nível atual.
- **Erro = depuração do pensamento**, nunca fracasso.
- **Roadmap vivo.** A cada marco fechado, os marcos restantes são recalibrados.

---

## 🇬🇧 English

### What's inside

Two components that split responsibilities:

| Component | File | Role |
|---|---|---|
| **Output style** (persona) | `.claude/output-styles/mentor-project.md` | Persistent session behavior — milestone-by-milestone conduct. |
| **Skill** (bootstrap) | `.claude/skills/new-project/` | A procedure you invoke once: demand → roadmap → skeleton. |

The skill pulls `reference.md` on demand (granularity, templates, layout), keeping
`SKILL.md` lean.

### How to use

1. Open Claude Code **inside this repository** (the files are locally scoped in `.claude/`).
2. Activate the persona:
   ```
   /output-style mentor-project
   ```
3. Bootstrap your learning project and describe in the chat what you want to build
   (attach a reference file, e.g. a target-design PDF, if you have one):
   ```
   /new-project
   ```

### Principles

- **Make it work → make it right → make it fast.** Best practices before it works are noise.
- **Vertical milestones, never themes.** Each milestone delivers something that runs/renders.
- **Conditional, just-in-time drills.** An isolated exercise only when the concept is new,
  non-trivial, and above the current level.
- **Error = debugging the thinking**, never failure.
- **Living roadmap.** At each closed milestone, the remaining milestones are recalibrated.

---

## Layout

```text
.claude/
├── output-styles/
│   ├── mentor-projeto.md      # persona (PT-BR)
│   └── mentor-project.md      # persona (EN)
└── skills/
    ├── novo-projeto/          # bootstrap (PT-BR): /novo-projeto
    │   ├── SKILL.md
    │   └── reference.md
    └── new-project/           # bootstrap (EN): /new-project
        ├── SKILL.md
        └── reference.md
```

> Para escopo global (vale em todo projeto), copie a pasta `.claude/` para `~/.claude/`.
> For global scope (applies to every project), copy the `.claude/` folder to `~/.claude/`.
