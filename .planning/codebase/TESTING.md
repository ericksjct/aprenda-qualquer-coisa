# TESTING — Aprenda Qualquer Coisa

> **Nao ha suite de testes automatizados neste repositorio.** Nenhum framework de
> teste, nenhum arquivo `test_*.py` / `*.test.*`, nenhum CI configurado. Isso e
> esperado para um toolkit de prompts em markdown — mas a "verificacao" existe em
> outras formas, descritas abaixo.

## Estado atual

- **Framework de teste:** nenhum (sem pytest, unittest, jest, etc.).
- **Arquivos de teste:** nenhum (`git ls-files` nao retorna nenhum).
- **CI/CD:** nenhum (`.github/workflows/` nao existe).
- **Cobertura:** N/A.
- **Linter/formatter configurado:** nenhum arquivo de config (`.ruff.toml`,
  `.flake8`, `.editorconfig`, `pyproject` ausentes).

## O unico codigo testavel: `scripts/roadmap_fetch.py`

E o unico alvo natural de teste automatizado e **hoje nao tem nenhum**. Se for
desejavel adicionar testes, os pontos de maior valor:

- **`build_outline(data)`** (`scripts/roadmap_fetch.py:43-112`) — funcao pura,
  testavel offline com um dict reactflow fixo (nodes + edges). Cobre: associacao
  subtopico→topico via BFS, fallback por posicao para orfaos, ordenacao por
  `(y, x)`. Maior densidade de logica = maior retorno de teste.
- **`render_markdown(slug, data, outline)`** (`:115-139`) — pura; titulo como dict
  vs string (`:117-119`) e um caso de borda real.
- **`fetch_roadmap(slug)`** (`:28-40`) — requer rede; testar com mock de
  `urllib.request.urlopen` ou um servidor local; verificar o tratamento de 404.

Sugestao de stack se for adicionar: `pytest` + fixtures JSON locais (mantendo a
filosofia stdlib para o codigo de producao; pytest so como dev dependency).

## "Verificacao" no metodo (testes de processo, nao de codigo)

O toolkit embute varios **checklists de verificacao** que funcionam como testes do
artefato pedagogico gerado — executados pelo agente, nao por uma maquina:

- **Verificacao de coesao do caminho** — checklist mecanico de 8 itens rodado no
  Passe 2 do bootstrap e em toda recalibragem (`mentor/reference.md:96-110`). Ex:
  "todo conceito em PRESSUPOE de P(N) e dominante de algum P(<N) ou coberto pelo
  substrato". Falhou → conserta o caminho antes de qualquer scaffold.
- **Validacao de scaffold antes de entregar** — 3 checagens obrigatorias
  (`mentor/reference.md:357-365`): PRESSUPOE so cita conceitos ja introduzidos;
  EXEMPLO-DE-RESULTADO e observavel; TODO descreve comportamento.
- **Definition of Done por marco** — criterios objetivos e verificaveis ("algo roda,
  renderiza, passa num check visual") — `mentor/reference.md:38-40`.
- **Checklist do aluno na aula** ("Para conferir antes de codar") —
  `mentor/reference.md:311-315`.

Estes sao a real "garantia de qualidade" do projeto: nao testam codigo, testam se o
material de ensino e coerente e bem calibrado antes de chegar ao aluno.

## Verificacao manual recomendada (gaps)

Como nao ha automacao, mudancas no toolkit dependem de revisao manual:

- **Consistencia de roteamento:** ao adicionar/renomear um procedimento em `mentor/`,
  conferir que `AGENTS.md` (tabela `:16-23`), o adaptador `.claude/skills/.../SKILL.md`
  e o `README.md` continuam apontando certo. Nada automatiza isso hoje.
- **Smoke do script:** `python scripts/roadmap_fetch.py frontend -o /tmp/` deve gerar
  um markdown nao-vazio (requer rede).
- **Links/paths em backticks:** caminhos citados no metodo devem existir no repo.
