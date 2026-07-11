# Aprenda Qualquer Coisa

**Um mentor de IA que te ensina a programar fazendo voce construir um projeto de
verdade** — em vez de escrever o codigo no seu lugar.

A ideia e simples: voce diz o que quer construir (um site, um joguinho, uma
planilha automatizada...) e o mentor monta o caminho de aprendizado, escreve uma
aula curta com a teoria minima de cada passo, prepara o esqueleto do codigo com
lacunas marcadas `TODO(human)` e te conduz a preencher cada uma — com perguntas,
pistas graduais e revisao **so depois que funciona**. Voce nunca fica adivinhando
sozinho: cada passo vem com a teoria que ele exige.
No fim, voce consegue explicar e mexer no que construiu sozinho.

> **Nunca programou? Sem problema.** O metodo foi feito pra comecar do zero: ele
> mede o que voce ja sabe antes de cada passo, entao nunca pressupoe o que voce
> ainda nao viu.

## Antes de comecar (pre-requisitos)

Voce precisa de **um agente de IA que rode no seu computador** e leia os arquivos
desta pasta. O recomendado e o **[Claude Code](https://code.claude.com)** (da
Anthropic) — instale-o seguindo o site oficial.

> Tambem funciona com Codex CLI, Kimi CLI, Cursor e qualquer agente que leia o
> arquivo `AGENTS.md`. Se voce usa um desses, pule pra secao
> "[Com outras ferramentas](#com-outras-ferramentas-codex-cli-kimi-cli-cursor)".

> _(Opcional: o mentor usa um pequeno script em Python 3 pra baixar mapas de
> conteudo da internet. Se voce tiver Python instalado, ele aproveita; se nao,
> segue funcionando sem.)_

## Comece aqui (Claude Code)

1. **Baixe esta pasta** pro seu computador e **abra-a no Claude Code** (abra o
   Claude Code de dentro desta pasta — e aqui que o projeto que voce vai aprender
   a construir vai morar).
2. **Ligue o modo mentor.** Digite `/config`, escolha **Output style** e
   selecione **mentor-projeto**. Isso troca o comportamento padrao ("a IA resolve
   pra voce") pelo modo mentor ("a IA te ensina a resolver"). Vale a partir da
   proxima sessao (ou depois de um `/clear`).
3. **Diga o que quer aprender a construir.** Digite `/novo-projeto` e descreva no
   chat. Se tiver uma referencia (ex: um print ou PDF do design que voce quer
   imitar), anexe. O mentor vai medir o que voce ja sabe, montar o caminho e
   preparar o primeiro pedaco.
4. **Pronto.** A partir daqui, **toda sessao de estudo comeca digitando
   `/tutor`** — ele lembra onde voce parou, conduz o passo do dia e revisa o que
   voce fez.

E so isso pra usar no dia a dia. As secoes seguintes ajudam, mas nao sao
obrigatorias.

> **Nao precisa instalar editor de codigo.** Quando o mentor te pedir pra editar um
> arquivo, de dois cliques em **`abrir-editor.cmd`** (nesta pasta): ele abre o editor
> no navegador, voce clica "Abrir pasta", escolhe esta pasta e edita ali mesmo, com
> cores e Ctrl+S — deixe a janelinha preta aberta enquanto edita. Pra ver uma pagina
> HTML sua funcionando, de dois cliques nela no Explorer. (Se voce ja usa VS Code ou
> outro editor, siga com ele — isso existe so pra ninguem travar por falta de
> ferramenta.)

## O dia a dia

Quase sempre voce so precisa do `/tutor` — ele chama as outras ferramentas
sozinho quando faz sentido. Mas, se quiser, da pra invocar na mao:

| Digite | Quando usar |
|---|---|
| `/tutor` | Sempre que voltar a estudar ("vamos continuar", "fiz, olha") |
| `/debug` | Quando algo nao funciona e voce nao sabe por que |
| `/fecha-marco` | Quando voce termina um marco (uma fatia do projeto) |
| `/spidr-split` | Quando um marco parece grande ou confuso demais |

O mentor cria **tres arquivos** no seu projeto pra se organizar. Voce nao precisa
edita-los, mas eles sao seus:

- **`CAMINHO.md`** — o plano do curso: todos os passos, na ordem certa.
- **`PROGRESSO.md`** — onde voce esta: o que ja sabe, o marco atual, o que falta.
- **`APRENDIZADO.md`** — seu diario: licoes, erros que voce ja resolveu, decisoes.

## Com outras ferramentas (Codex CLI, Kimi CLI, Cursor...)

1. Abra a ferramenta **de dentro desta pasta**. Quem le `AGENTS.md` (Codex, Kimi,
   Cursor e outros) ja assume o papel de mentor sozinho.
2. **Nao tem comandos com barra.** Fale natural — o `AGENTS.md` entende a
   situacao:

   ```text
   "quero aprender a construir X"      -> comeca um projeto novo
   "vamos continuar" / "fiz, olha"     -> sessao de tutoria
   "terminei o marco"                  -> fechamento do marco
   "ta dando erro e nao sei por que"   -> investigacao do erro
   ```

3. Se a sua ferramenta usa outro arquivo de contexto (ex: `GEMINI.md`), crie esse
   arquivo com uma linha: "Leia e siga `AGENTS.md`".

## Palavrinhas que aparecem aqui

- **Marco** — uma fatia do projeto que, quando pronta, ja faz algo visivel
  funcionar (ex: "os 3 cards aparecem lado a lado"). O projeto avanca marco a
  marco, e nunca um marco e so "teoria".
- **Aula** — um arquivo curto em markdown que o mentor escreve para cada passo, com
  a teoria minima pra voce concluir aquele passo sem buscar na internet nem espiar a
  pista. Voce le a aula antes de mexer no scaffold.
- **Scaffold** — o esqueleto de codigo que o mentor monta pra voce, com lacunas
  marcadas pra voce preencher.
- **`TODO(human)`** — o marcador que aponta exatamente o trecho que e VOCE quem
  escreve. O mentor nunca preenche esses por voce.
- **Substrato** — o que voce ja domina de cada assunto. O mentor mede isso antes
  de ensinar, pra nao pular etapas nem te encher de obvio.
- **Modo estudo** — pra quando voce quer dominar um assunto SEM construir nada (ex:
  estudar pelo livro pra uma prova): o mentor monta a programacao de aulas, ensina a
  teoria, tira duvidas e te faz praticar com exercicios em niveis — voce demonstra o
  dominio resolvendo e explicando, em vez de codar. E escolhido no `/novo-projeto`.
- **Persona / modo mentor** — o ajuste (passo 2 acima) que faz a IA ensinar em
  vez de resolver no seu lugar.

---

## Como funciona por dentro

_(daqui pra baixo e pra quem quer entender, manter ou portar o toolkit.)_

O toolkit e **agnostico de LLM**: o metodo vive em markdown neutro (`mentor/`) e
cada ferramenta tem so um adaptador fino apontando pra ele.

| Componente | Arquivo | Papel |
|---|---|---|
| **Metodo** (fonte unica) | `mentor/` | Persona (`metodo.md`) + procedimentos (`novo-projeto`, `tutor`, `fecha-marco`, `debug`, `spidr-split`, `estudo`) + templates (`reference.md`). |
| **Entrada universal** | `AGENTS.md` | Lido automaticamente por Codex CLI, Kimi CLI, Cursor e outros: define o papel e roteia cada situacao para o arquivo de `mentor/`. |
| **Adaptadores Claude Code** | `.claude/` | Output style + skills finas (`/novo-projeto`, `/tutor`, `/fecha-marco`, `/debug`, `/spidr-split`, `/converte-livro`) que apontam para `mentor/`. |
| **Script** (referencia) | `scripts/roadmap_fetch.py` | Baixa roadmaps do [roadmap.sh](https://roadmap.sh) como base de ordenacao canonica de conceitos. So precisa de Python 3 (stdlib). |

Os procedimentos do metodo:

| Procedimento | Quando |
|---|---|
| `mentor/novo-projeto.md` | Bootstrap: demanda -> sondagem de substrato -> caminho completo (`CAMINHO.md`) -> marcos -> esqueleto. |
| `mentor/tutor.md` | Copiloto de sessao: restaura contexto, conduz o passo atual, revisa tentativas, fecha a sessao com log. |
| `mentor/fecha-marco.md` | Fechamento: done -> curadoria -> tag -> recalibragem -> proximo. |
| `mentor/debug.md` | Protocolo de forense para transformar erros em aprendizado. |
| `mentor/spidr-split.md` | Quebra marcos grandes em fatias usando SPIDR Splitting. |

Os procedimentos puxam o `reference.md` sob demanda (granularidade, templates,
layout), mantendo cada arquivo enxuto.

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
abrir-editor.cmd               # DOIS CLIQUES: abre o editor no navegador (serve o ide.html em localhost)
ide.html                       # o editor em si (Monaco + File System Access API; exige localhost)
mentor/                        # METODO — fonte unica, markdown neutro
├── metodo.md                  # persona/conduta permanente
├── novo-projeto.md            # bootstrap (2 passes: caminho -> marcos)
├── tutor.md                   # copiloto de sessao
├── fecha-marco.md             # fechamento de marco
├── debug.md                   # protocolo de forense
├── spidr-split.md             # decomposicao de marcos
├── estudo.md                  # modo estudo: teoria sem projeto (modulos, exercicios, teach-back)
└── reference.md               # templates (CAMINHO, PROGRESSO, scaffold) e regras
.claude/                       # adaptadores Claude Code (apontam para mentor/)
├── output-styles/
│   └── mentor-projeto.md      # persona: ative via /config -> Output style
└── skills/
    ├── novo-projeto/SKILL.md  # /novo-projeto
    ├── tutor/SKILL.md         # /tutor
    ├── spidr-split/SKILL.md   # /spidr-split
    ├── fecha-marco/SKILL.md   # /fecha-marco
    ├── debug/SKILL.md         # /debug
    └── converte-livro/SKILL.md  # /converte-livro (opcional; aponta para novo-projeto.md)
scripts/
├── roadmap_fetch.py           # python scripts/roadmap_fetch.py <slug> -o .projetos/<slug>/referencias/
├── converte_livro.py          # python scripts/converte_livro.py <pdf> --slug <slug>  (opcional, venv)
└── valida_artefato.py         # python scripts/valida_artefato.py <arquivo>  (check mecanico: campos do scaffold + markdownlint basico)
.projetos/                     # casa dos projetos (no .gitignore: pessoais, NAO sobem
└── <slug>/                    #   pro github do toolkit). Cada projeto e seu proprio
                               #   repo git: CAMINHO, PROGRESSO, aulas/, projeto/, exercicios/...
```

Dentro de `.projetos/<slug>/`, o bootstrap gera **tres** documentos centrais:

- `CAMINHO.md` — design: todos os passos do aprendizado (conceito, pressupostos,
  entregavel) + mapa passos -> marcos.
- `PROGRESSO.md` — acompanhamento: tabela de substrato por assunto, DoD, marcos,
  dividas e log.
- `APRENDIZADO.md` — diario do aluno: licoes, padroes de erro, decisoes.

Alem deles, a pasta `aulas/` recebe uma aula por passo (`P0x-<slug>.md`) com a teoria
minima daquele passo — geradas no bootstrap e atualizadas quando o caminho recalibra.

> Os adaptadores apontam para `mentor/` por caminho relativo a raiz do repo — por isso
> o escopo e local: use o toolkit abrindo a ferramenta dentro deste repositorio (os
> projetos do aluno vivem em `.projetos/<slug>/`). Para usar noutro repo, copie `mentor/`,
> `AGENTS.md`, `scripts/` e (para Claude Code) `.claude/` juntos.
