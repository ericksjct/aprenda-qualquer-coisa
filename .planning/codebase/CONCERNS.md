# CONCERNS — Aprenda Qualquer Coisa

> Divida tecnica, fragilidades e areas de atencao. Como o "produto" e um conjunto de
> instrucoes em markdown consumidas por um LLM, os riscos sao majoritariamente de
> **consistencia documental, deriva (drift) e portabilidade** — nao bugs de runtime.

## Risco #1 — Consistencia entre fonte unica e adaptadores (drift)

O design "fonte unica + adaptadores finos" depende de disciplina manual. Nada impede,
mecanicamente, que:

- um procedimento seja renomeado em `mentor/` e o ponteiro em `AGENTS.md:16-23`,
  numa skill `.claude/skills/.../SKILL.md`, ou no `README.md` fique apontando para o
  nome velho;
- o `README.md` (`:114-129`), o `AGENTS.md` (`:16-23`) e o `mentor/metodo.md`
  descrevam o conjunto de procedimentos de formas que divergem com o tempo.

**Mitigacao atual:** nenhuma automacao. **Sugestao:** um script de verificacao que
confira que todo `/comando` citado tem `mentor/<comando>.md` correspondente e um
adaptador, e que os caminhos em backticks existem. Hoje e 100% revisao humana
(ver `TESTING.md`).

## Risco #2 — Acoplamento por caminho relativo (escopo local)

Os adaptadores apontam para `mentor/` por **caminho relativo a raiz do repo**
(`README.md:196-199`). Consequencia documentada: o toolkit so funciona se a ferramenta
for aberta **dentro deste repositorio**. Para usar noutro repo, e preciso copiar
`mentor/`, `AGENTS.md`, `scripts/` e `.claude/` juntos. E uma limitacao assumida, mas
torna o toolkit fragil a:

- mover/renomear pastas de topo (quebra todos os ponteiros silenciosamente);
- usar so parte dos arquivos (copia incompleta → procedimento referenciado some).

## Risco #3 — Dependencia de um endpoint externo nao-versionado

`scripts/roadmap_fetch.py` depende do formato JSON reactflow de
`https://roadmap.sh/<slug>.json` (`:25`). Riscos:

- **Mudanca de schema upstream** — se roadmap.sh alterar `nodes`/`edges`/`type`/
  `position`, `build_outline` (`:43-112`) pode silenciosamente produzir um outline
  vazio ou errado. Ha sys.exit para "sem topicos extraiveis" (`:155-156`), mas nao
  para um outline parcial/degradado.
- **Sem cache/fixture versionado** — nenhum exemplo de resposta salvo no repo, entao
  uma regressao do parser nao tem como ser detectada sem rede (ver `TESTING.md`).
- **Mitigacao existente:** o passo e explicitamente **opcional** — o metodo segue sem
  o script (`mentor/novo-projeto.md:50`). Logo o impacto e degradacao graciosa, nao
  quebra do fluxo principal.

## Risco #4 — Eficacia depende da adesao do agente (nao e enforced)

A regra de ouro ("nunca preencha o `TODO(human)`") e os anti-padroes
(`mentor/metodo.md:141-165`) sao **instrucoes**, nao garantias. Um modelo mais fraco,
um output style desativado, ou um host que nao carrega `mentor/metodo.md` no inicio da
sessao podem resultar no agente resolvendo o exercicio pelo aluno — exatamente o
fracasso que o toolkit existe para evitar. Pontos sensiveis:

- No Claude Code, a persona so vale **apos** ativar o Output style via `/config`
  (`README.md:38-40`) — facil de esquecer; se nao ativada, comportamento padrao
  ("a IA resolve") prevalece.
- Em agentes via `AGENTS.md`, depende do agente realmente ler e obedecer o arquivo.

## Risco #5 — Idioma sem acentos e encoding

Todo o conteudo usa portugues **sem acentos** (deliberado, por robustez de encoding).
E uma escolha consciente, mas: (a) reduz legibilidade; (b) se um contribuidor futuro
introduzir acentos misturados, a inconsistencia pode confundir. Nao ha lint que
imponha o padrao.

## Pontos frageis no codigo (`scripts/roadmap_fetch.py`)

- **`render_markdown` assume `data.get("title")`** podendo ser dict (`:117-119`) — ja
  tratado, mas sinaliza que o schema upstream e instavel/variavel.
- **BFS + fallback por posicao** (`:62-94`) e heuristico: a associacao
  subtopico→topico por proximidade pode errar em layouts atipicos. Sem teste que trave
  uma regressao.
- **Timeout fixo de 30s** sem retry (`:32`) — falha de rede transiente aborta o passo
  (aceitavel, dado que e opcional).

## O que NAO e preocupacao (para evitar alarme falso)

- **Sem segredos no repo** — `roadmap_fetch.py` nao usa API key; nao ha `.env`. O
  `.gitignore` ja protege `CLAUDE.md` e `.projetos/` (dados pessoais do aluno).
- **Sem superficie de ataque de runtime** — nao ha servidor, banco, nem input nao
  confiavel processado em producao (o unico IO de rede e um GET read-only opcional).
- **Sem divida de performance** — nada roda em escala; o script processa um JSON pequeno.

## Resumo de prioridade

| Prioridade | Concern | Acao sugerida |
|---|---|---|
| Alta | Drift fonte↔adaptadores (#1) | Script de verificacao de consistencia de ponteiros |
| Media | Schema upstream do roadmap.sh (#3) | Salvar fixture JSON + teste de `build_outline` |
| Media | Persona nao ativada por engano (#4) | Reforcar checagem de ativacao no inicio da sessao |
| Baixa | Acoplamento por caminho relativo (#2) | Documentado; aceitar ou parametrizar raiz |
