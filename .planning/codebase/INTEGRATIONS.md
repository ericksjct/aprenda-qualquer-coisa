# INTEGRATIONS — Aprenda Qualquer Coisa

> Servicos externos, APIs e integracoes. Este toolkit e quase totalmente
> auto-contido (markdown lido por um agente). Ha **uma unica integracao externa
> real** e algumas integracoes de "host" (o ambiente do agente de IA).

## Integracoes externas reais

### roadmap.sh (HTTP GET, somente leitura)

- **Onde:** `scripts/roadmap_fetch.py`
- **Endpoint:** `https://roadmap.sh/{slug}.json` (`scripts/roadmap_fetch.py:25`)
- **Protocolo:** HTTP GET via `urllib.request` (stdlib), header
  `User-Agent: roadmap-fetch/1.0`, timeout 30s (`scripts/roadmap_fetch.py:29-33`).
- **Formato:** JSON publico no formato reactflow (`nodes` + `edges`). Sem API key,
  sem autenticacao, sem scraping de HTML — e um endpoint JSON publico.
- **Tratamento de erro:** 404 -> mensagem amigavel sugerindo conferir o slug
  (`scripts/roadmap_fetch.py:34-40`); demais HTTPError sao propagados.
- **Uso no fluxo:** chamado no bootstrap (`mentor/novo-projeto.md`, Passo 3) para obter
  a ordenacao canonica de conceitos de uma stack. **Opcional** — se indisponivel, o
  metodo segue sem (`mentor/novo-projeto.md:50`).
- **Saida:** grava `roadmap-<slug>.md` em `.projetos/<slug>/referencias/`.

## Integracoes de host (o ambiente do agente)

Estas nao sao APIs chamadas por codigo, mas pontos de acoplamento com a ferramenta
que executa o toolkit:

- **Claude Code** — le `.claude/output-styles/mentor-projeto.md` (ativado via
  `/config` -> Output style) e as skills em `.claude/skills/*/SKILL.md` (comandos
  `/novo-projeto`, `/tutor`, `/fecha-marco`, `/debug`, `/spidr-split`).
- **Agentes que leem `AGENTS.md`** (Codex CLI, Kimi CLI, Cursor) — `AGENTS.md` e a
  entrada universal; o agente assume o papel de mentor automaticamente
  (`AGENTS.md:61-62`, `README.md:71-86`).
- **Outros agentes com arquivo de contexto proprio** (ex: `GEMINI.md`) — instrucao e
  apontar/copiar para `AGENTS.md` (`AGENTS.md:63-64`).
- **git** — usado pelo metodo (nao por codigo do toolkit) para versionar cada projeto
  do aluno e marcar marcos como tags `marco-NN-<slug>` no repo do proprio projeto
  (`mentor/reference.md:158-165`).

## O que NAO existe (e por que importa para o planejamento)

- **Banco de dados:** nenhum. Estado do aluno mora em arquivos markdown
  (`PROGRESSO.md`, `CAMINHO.md`, `APRENDIZADO.md`) dentro de `.projetos/<slug>/`.
- **Autenticacao / providers de auth:** nenhum.
- **Webhooks / filas / mensageria:** nenhum.
- **Provider de LLM acoplado:** **nenhum, por design.** O toolkit e explicitamente
  agnostico de LLM (`README.md:111-112`). O metodo nao chama nenhuma API de modelo;
  ele E o conteudo que um modelo qualquer consome.
- **Telemetria / analytics:** nenhum.
