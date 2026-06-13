# Aprenda Qualquer Coisa

> Toolkit **agnostico de LLM** de mentoria de aprendizado por projeto. Funciona com
> [Claude Code](https://code.claude.com), Codex CLI, Kimi CLI, Cursor e qualquer
> agente que leia `AGENTS.md`.

Em vez de o agente escrever o codigo por voce, ele **conduz voce a escreve-lo**: desenha a
estrutura, deixa marcadores `TODO(human)`, faz perguntas socraticas e so sugere melhorias
**depois que o codigo funciona**. O projeto e o laboratorio; o objetivo e voce conseguir
explicar e estender o que construiu sozinho.

## O que tem aqui

O toolkit e **agnostico de LLM**: o metodo vive em markdown neutro (`mentor/`) e
cada ferramenta tem so um adaptador fino apontando pra ele.

| Componente | Arquivo | Papel |
|---|---|---|
| **Metodo** (fonte unica) | `mentor/` | Persona (`metodo.md`) + procedimentos (`novo-projeto`, `tutor`, `fecha-marco`, `debug`, `spidr-split`) + templates (`reference.md`). |
| **Entrada universal** | `AGENTS.md` | Lido automaticamente por Codex CLI, Kimi CLI, Cursor e outros: define o papel e roteia cada situacao para o arquivo de `mentor/`. |
| **Adaptadores Claude Code** | `.claude/` | Output style + skills finas (`/novo-projeto`, `/tutor`, `/fecha-marco`, `/debug`, `/spidr-split`) que apontam para `mentor/`. |
| **Script** (referencia) | `scripts/roadmap_fetch.py` | Baixa roadmaps do [roadmap.sh](https://roadmap.sh) como base de ordenacao canonica de conceitos. So precisa de Python 3 (stdlib). |

Os procedimentos do metodo:

| Procedimento | Quando |
|---|---|
| `mentor/novo-projeto.md` | Bootstrap: demanda -> sondagem de substrato -> caminho completo (`CAMINHO.md`) -> marcos -> esqueleto. |
| `mentor/tutor.md` | Copiloto de sessao: restaura contexto, conduz o passo atual, revisa tentativas, fecha a sessao com log. |
| `mentor/fecha-marco.md` | Fechamento: done -> curadoria -> tag -> recalibragem -> proximo. |
| `mentor/debug.md` | Protocolo de forense para transformar erros em aprendizado. |
| `mentor/spidr-split.md` | Quebra marcos grandes em fatias usando SPIDR Splitting. |

A skill puxa `reference.md` sob demanda (granularidade, templates, layout), mantendo o
`SKILL.md` enxuto.

## Como usar

### Com Claude Code

1. Abra o Claude Code **dentro deste repositorio** (os arquivos tem escopo local em `.claude/`).
2. Ative a persona **mentor-projeto** (uma vez por projeto): rode `/config`,
   escolha **Output style** e selecione **mentor-projeto**. Sem menu, adicione
   o campo abaixo em `.claude/settings.local.json` (efetivo após `/clear` ou
   nova sessão):

   ```json
   { "outputStyle": "mentor-projeto" }
   ```

3. Faca o bootstrap do seu projeto de aprendizado e descreva no chat o que quer construir
   (anexe um arquivo de referencia, ex.: um PDF de design-alvo, se tiver):

   ```text
   /novo-projeto
   ```

4. Depois do bootstrap, **toda sessao de estudo comeca com o tutor copiloto**:

   ```text
   /tutor                # restaura onde voce parou, conduz o passo atual e revisa
   ```

5. Durante o projeto, use as skills auxiliares conforme necessario (o `/tutor`
   roteia para elas automaticamente):

   ```text
   /spidr-split          # quando um marco parece grande demais
   /fecha-marco          # quando voce termina um marco
   /debug                # quando esta travado num erro
   ```

### Com Codex CLI, Kimi CLI, Cursor e outros

1. Abra a ferramenta **dentro deste repositorio**. Ferramentas que leem `AGENTS.md`
   (Codex CLI, Kimi CLI, Cursor, entre outras) ja assumem o papel de mentor
   automaticamente.
2. Nao ha slash commands: fale naturalmente. O `AGENTS.md` roteia cada situacao
   para o procedimento certo de `mentor/`:

   ```text
   "quero aprender a construir X"   -> bootstrap (mentor/novo-projeto.md)
   "vamos continuar" / "fiz, olha"  -> sessao de tutoria (mentor/tutor.md)
   "terminei o marco"               -> fechamento (mentor/fecha-marco.md)
   "ta dando erro e nao sei por que" -> forense (mentor/debug.md)
   ```

3. Se a ferramenta usa outro arquivo de contexto (ex: `GEMINI.md`), crie esse
   arquivo com uma linha: "Leia e siga `AGENTS.md`".

## Principios

- **Caminho completo antes dos modulos.** O `CAMINHO.md` expande TODOS os passos
  (conceito dominante, pressupostos, entregavel) antes de agrupar em marcos. So assim
  da pra garantir que o passo N nao pressupoe o que nunca foi ensinado.
- **Sondagem, nao autoavaliacao.** O nivel por assunto e medido com sondas praticas
  (snippet, producao, vocabulario) e registrado em tabela. Scaffold se calibra por ela.
- **Entregavel observavel.** Cada passo e cada marco dizem o que o aluno VE funcionando
  ("os 3 cards ficam lado a lado"), nunca so o que ele "aprende".
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
AGENTS.md                      # entrada universal (Codex, Kimi, Cursor, ...)
mentor/                        # METODO — fonte unica, markdown neutro
├── metodo.md                  # persona/conduta permanente
├── novo-projeto.md            # bootstrap (2 passes: caminho -> marcos)
├── tutor.md                   # copiloto de sessao
├── fecha-marco.md             # fechamento de marco
├── debug.md                   # protocolo de forense
├── spidr-split.md             # decomposicao de marcos
└── reference.md               # templates (CAMINHO, PROGRESSO, scaffold) e regras
.claude/                       # adaptadores Claude Code (apontam para mentor/)
├── output-styles/
│   └── mentor-projeto.md      # persona: ative via /config -> Output style
└── skills/
    ├── novo-projeto/SKILL.md  # /novo-projeto
    ├── tutor/SKILL.md         # /tutor
    ├── spidr-split/SKILL.md   # /spidr-split
    ├── fecha-marco/SKILL.md   # /fecha-marco
    └── debug/SKILL.md         # /debug
scripts/
└── roadmap_fetch.py           # python scripts/roadmap_fetch.py <slug> -o referencias/
```

No repo do aluno, o bootstrap gera dois documentos centrais:

- `CAMINHO.md` — design: todos os passos do aprendizado (conceito, pressupostos,
  entregavel) + mapa passos -> marcos.
- `PROGRESSO.md` — acompanhamento: tabela de substrato por assunto, DoD, marcos,
  dividas e log.

> Os adaptadores apontam para `mentor/` por caminho relativo a raiz do repo — por isso
> o escopo e local: use o toolkit abrindo a ferramenta dentro deste repositorio (o
> projeto do aluno vive aqui dentro). Para usar noutro repo, copie `mentor/`, `AGENTS.md`,
> `scripts/` e (para Claude Code) `.claude/` juntos.
