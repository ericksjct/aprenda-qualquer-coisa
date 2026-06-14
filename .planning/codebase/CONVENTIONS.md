# CONVENTIONS — Aprenda Qualquer Coisa

> Estilo, nomes e padroes. Como ~83% do repo e prosa em markdown, as convencoes mais
> importantes sao **editoriais/pedagogicas**, nao de codigo. Seguem ambas.

## Convencoes de escrita (markdown — o substrato dominante)

- **Idioma:** portugues, predominantemente **sem acentos** (ex: "voce", "metodo",
  "codigo"). Consistente em todo `mentor/`, `AGENTS.md`, `README.md`. Provavelmente
  escolha deliberada para evitar problemas de encoding entre ferramentas/terminais.
- **Tom:** segunda pessoa, imperativo e direto ("leia esse arquivo agora", "nunca
  escreva o trecho de codigo"). O metodo fala COM o agente, instruindo conduta.
- **Codigo/identificadores inline:** sempre em backticks — `TODO(human)`, `CAMINHO.md`,
  `mentor/metodo.md`, `/tutor`. Padrao rigorosamente seguido; replique-o.
- **Caminhos de arquivo:** sempre relativos a raiz do repo e em backticks.
- **Blocos de exemplo:** cercados com linguagem (` ```markdown `, ` ```text `,
  ` ```bash `). Templates longos vivem em `mentor/reference.md` como blocos ` ```markdown `.
- **Enfase semantica:** **negrito** para conceitos-chave e regras inegociaveis;
  > blockquotes para notas de contrato/aviso no topo de secoes.
- **Tabelas** para roteamento e mapeamentos (situacao→procedimento, componente→arquivo).

## Convencoes estruturais (o metodo em si)

Estas sao "convencoes" que o agente DEVE aplicar ao gerar artefatos do aluno:

- **Regra de ouro (inviolavel):** nunca preencher o `TODO(human)` — `mentor/metodo.md:12-16`.
- **Formato de scaffold fixo:** campos META → PORQUE → PRESSUPOE → ARQUIVOS →
  EXEMPLO-DE-RESULTADO → DONE → PERGUNTA-GUIA → TODO → PISTA. Ordem e obrigatoria;
  template em `mentor/reference.md:337-353`.
- **IDs estaveis:** conceitos `c0x-slug`, passos `P0x`, marcos `marco-NN-slug`. Nunca
  renumere retroativamente sem recalibrar referencias.
- **Entregavel observavel:** todo passo/marco descreve o que o aluno VE, nunca so o que
  "aprende" (`README.md:140-142`, anti-padrao em `mentor/metodo.md:164`).
- **Comentario adapta a linguagem-alvo:** o bloco de scaffold usa a sintaxe de
  comentario da linguagem do aluno (`mentor/reference.md:336`).

## Padrao de adaptador (replicar ao adicionar suporte a nova ferramenta)

Todo adaptador e **fino e nao duplica conteudo**:

```markdown
---
name: <comando>
description: <quando usar — 1 frase, gatilhos entre aspas>
---

# <Titulo> (adaptador Claude Code)

Leia `mentor/<comando>.md` ... e siga o procedimento exatamente.
Convencao: quando o documento citar um `/comando`, e a skill correspondente
(conteudo canonico em `mentor/<comando>.md`).
```

Exemplo de referencia: `.claude/skills/tutor/SKILL.md`. **Anti-padrao:** copiar logica
do metodo para dentro do adaptador (quebra a fonte unica).

## Convencoes de codigo Python (`scripts/roadmap_fetch.py`)

Unico arquivo de codigo; estabelece o padrao para qualquer script futuro:

- **Stdlib apenas** — sem dependencias externas (decisao deliberada, ver `STACK.md`).
- **Type hints modernos** — `list[dict]`, `dict[str, set[str]]`, anotacoes de retorno
  `-> dict` (`scripts/roadmap_fetch.py:28,43`).
- **Docstring de modulo** rica, com secao "Uso:" e exemplos — `:1-16`.
- **Funcoes puras pequenas e nomeadas:** `fetch_roadmap`, `build_outline`,
  `render_markdown`, `main` — separacao clara IO ↔ transformacao ↔ render.
- **CLI via `argparse`** com `--out-dir` default sensato (`:142-151`).
- **Erros amigaveis ao usuario** via `sys.exit("mensagem em portugues")` em vez de
  traceback cru para o caso esperado (404) — `:34-40,155`.
- **Comentarios explicam o "porque"** do algoritmo (BFS de subtopicos, fallback por
  posicao) — `:49-52,79-80`.
- **`encoding="utf-8"` explicito** na escrita (`:161`).

## Tratamento de erro (geral)

- **No codigo:** distingue erro esperado (404 → mensagem clara) de inesperado
  (re-raise). Sem `except` mudo.
- **No metodo (pedagogico):** erro do aluno NUNCA e tratado como fracasso — vira o
  "protocolo de forense" de 6 passos (`mentor/metodo.md:77-89`, `mentor/debug.md`).
