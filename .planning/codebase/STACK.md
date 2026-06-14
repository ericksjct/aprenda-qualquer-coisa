# STACK — Aprenda Qualquer Coisa

> Mapa de tecnologias e dependencias. **Nota importante:** este NAO e um codebase de
> software executavel. E um **toolkit de prompts/metodo em markdown** ("Mentor de
> Aprendizado por Projeto") consumido por agentes de IA (Claude Code, Codex CLI, etc.).
> A maior parte das categorias de "stack" tradicional (framework web, banco, build,
> runtime de servidor) **nao se aplica**. O que existe esta listado abaixo.

## Natureza do artefato

| Aspecto | Realidade |
|---|---|
| Tipo de projeto | Toolkit de instrucoes para agentes de IA (prompt engineering em markdown) |
| Linguagem dominante | **Markdown** (15 dos 18 arquivos versionados) |
| Linguagem de codigo | **Python 3** (1 script utilitario: `scripts/roadmap_fetch.py`) |
| Runtime | Nenhum servidor/app. O "runtime" e o **agente de IA** que le os arquivos |
| Build / compile | Nenhum. Os arquivos sao lidos como contexto pelo LLM |
| Distribuicao | Repositorio git copiado para a maquina do usuario; aberto dentro do agente |

## Linguagens e versoes

- **Markdown** (GitHub-flavored) — substrato de todo o metodo (`mentor/*.md`),
  da entrada universal (`AGENTS.md`), dos adaptadores Claude Code (`.claude/**/*.md`)
  e da documentacao (`README.md`).
- **Python 3** — apenas `scripts/roadmap_fetch.py`. Usa somente a **stdlib**
  (`argparse`, `json`, `sys`, `urllib.request`, `urllib.error`, `pathlib`). Type hints
  com sintaxe `list[dict]` / `dict[str, set[str]]` exigem **Python 3.9+**.

## Dependencias

**Zero dependencias de terceiros.** Nao ha `requirements.txt`, `pyproject.toml`,
`package.json`, `Cargo.toml` nem lockfiles. O unico codigo executavel
(`scripts/roadmap_fetch.py`) roda apenas com a biblioteca padrao do Python — por
design, para que o script seja opcional e nao exija setup (ver `README.md:28-30`).

## "Dependencias" reais do toolkit (nao-codigo)

O que o toolkit de fato precisa para funcionar:

- **Um agente de IA host** que leia arquivos do diretorio. Recomendado:
  **Claude Code** (`README.md:20-23`). Tambem suportado: qualquer agente que leia
  `AGENTS.md` (Codex CLI, Kimi CLI, Cursor — `README.md:71-86`).
- **Python 3** (opcional) — so para o `roadmap_fetch.py`; o toolkit "segue funcionando
  sem" (`README.md:28-30`).
- **Acesso a internet** (opcional) — `roadmap_fetch.py` busca JSON publico de
  `https://roadmap.sh/<slug>.json` (`scripts/roadmap_fetch.py:25`).

## Configuracao

- `.claude/settings.local.json` — configuracoes locais do Claude Code (nao versionado
  como parte do metodo; especifico da maquina).
- `aprenda-qualquer-coisa.code-workspace` — arquivo de workspace do VS Code (49 bytes).
- `.gitignore` — ignora `CLAUDE.md` e `.projetos/` (ver `STRUCTURE.md` e `CONCERNS.md`).
- **Frontmatter YAML** nos arquivos de skill/output-style (`.claude/**/*.md`): campos
  `name` e `description` — o unico "formato estruturado" do repo.

## Como rodar o unico codigo executavel

```bash
python scripts/roadmap_fetch.py <slug> -o .projetos/<slug>/referencias/
# ex: python scripts/roadmap_fetch.py frontend -o .projetos/meu-site/referencias/
```

Baixa um roadmap de `roadmap.sh`, extrai os topicos em ordem de leitura canonica
(formato reactflow: nodes + edges) e grava um markdown enxuto usado como base de
ordenacao de conceitos no bootstrap (`mentor/novo-projeto.md`, Passo 3).
