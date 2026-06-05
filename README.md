# Aprenda Qualquer Coisa

> Toolkit de **mentoria de aprendizado por projeto** para o [Claude Code](https://code.claude.com).

Em vez de o agente escrever o codigo por voce, ele **conduz voce a escreve-lo**: desenha a
estrutura, deixa marcadores `TODO(human)`, faz perguntas socraticas e so sugere melhorias
**depois que o codigo funciona**. O projeto e o laboratorio; o objetivo e voce conseguir
explicar e estender o que construiu sozinho.

## O que tem aqui

Um output style (persona) + quatro skills auxiliares:

| Componente | Arquivo | Papel |
|---|---|---|
| **Output style** (persona) | `.claude/output-styles/mentor-projeto.md` | Comportamento persistente da sessao — conduta marco a marco. |
| **Skill** (bootstrap) | `.claude/skills/novo-projeto/` | Procedimento invocavel uma vez: demanda -> roadmap -> esqueleto. |
| **Skill** (decomposicao) | `.claude/skills/spidr-split/` | Quebra marcos grandes em fatias usando SPIDR Splitting. |
| **Skill** (fechamento) | `.claude/skills/fecha-marco/` | Fecha marco de forma sistematica: done -> curadoria -> tag -> proximo. |
| **Skill** (debug) | `.claude/skills/debug/` | Protocolo de forense para transformar erros em aprendizado. |

A skill puxa `reference.md` sob demanda (granularidade, templates, layout), mantendo o
`SKILL.md` enxuto.

## Como usar

1. Abra o Claude Code **dentro deste repositorio** (os arquivos tem escopo local em `.claude/`).
2. Ative a persona:

   ```text
   /output-style mentor-projeto
   ```

3. Faca o bootstrap do seu projeto de aprendizado e descreva no chat o que quer construir
   (anexe um arquivo de referencia, ex.: um PDF de design-alvo, se tiver):

   ```text
   /novo-projeto
   ```

4. Durante o projeto, use as skills auxiliares conforme necessario:

   ```text
   /spidr-split          # quando um marco parece grande demais
   /fecha-marco          # quando voce termina um marco
   /debug                # quando esta travado num erro
   ```

## Principios

- **Make it work -> make it right -> make it fast.** Best-practice antes de funcionar e ruido.
- **Marcos verticais, nunca temas.** Cada marco entrega algo que roda/renderiza.
- **User Story por marco.** Cada marco e enquadrado como: "Como [usuario], eu quero
  [capacidade], para que [valor]."
- **Walking Skeleton.** O primeiro marco e o esqueleto ambulante mais fino que prova que
  todas as camadas funcionam juntas.
- **Drill condicional, just-in-time.** Exercicio isolado so quando o conceito e novo,
  nao-trivial e acima do nivel atual.
- **Erro = depuracao do pensamento**, nunca fracasso. Protocolo de forense de 6 passos.
- **Roadmap vivo.** A cada marco fechado, os marcos restantes sao recalibrados.
- **Demanda-First.** Nenhum codigo antes da demanda estar clara e aprovada.
- **Substrato por assunto, nao por aluno.** Zero-absoluto num assunto nao e o mesmo que
  iniciante. Descoberta socratica so funciona com materia-prima pra raciocinar.

## Layout

```text
.claude/
├── output-styles/
│   └── mentor-projeto.md      # persona: /output-style mentor-projeto
└── skills/
    ├── novo-projeto/          # bootstrap: /novo-projeto
    │   ├── SKILL.md
    │   └── reference.md
    ├── spidr-split/           # decomposicao: /spidr-split
    │   └── SKILL.md
    ├── fecha-marco/           # fechamento: /fecha-marco
    │   └── SKILL.md
    └── debug/                 # forense: /debug
        └── SKILL.md
```

> Para escopo global (vale em todo projeto), copie a pasta `.claude/` para `~/.claude/`.
