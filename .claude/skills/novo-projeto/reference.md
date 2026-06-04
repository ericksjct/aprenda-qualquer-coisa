# Referencia — Mentor de Projeto

## Regra de granularidade
- Unidade = **1 capacidade coesa**, nao 1 atomo de conceito. Teste: ao fechar a unidade,
  o aluno consegue articular UM "porque" inteiro.
- **Criterio de fechamento verificavel**: cada unidade tem um "done" objetivo (algo roda,
  renderiza, passa num check visual). Check verde so vale se houve sintese.
- **Tamanho**: completavel numa sessao focada (~30-90 min). Maior -> quebre; menor -> funda.
- **Salto suave**: cada unidade introduz no maximo 1 conceito dominante novo e reusa os
  anteriores. Sem degraus.
- **Granularidade ~ 1/nivel**: iniciante -> unidades menores + mais andaime; avancado ->
  unidades maiores + mais buraco a preencher.

## Marcos verticais, nunca temas
Nao organize por tema puro (`01-html/`, `02-css/`, `03-js/`). Isso recria o curso
tradicional: o aluno aprende um assunto inteiro antes de saber pra que -> salto de
motivacao e de integracao. Cada marco e uma **fatia vertical** que atravessa varios
assuntos mas sempre entrega algo visivel e funcional.

## Drill condicional (`exercicios/`)
- Gere SO quando: conceito novo x nao-trivial x acima do nivel atual.
- **Angulo diferente** da aplicacao: drill = intuicao do mecanismo isolado; aplicacao =
  decisao/integracao no artefato. O drill nunca deve entregar a resposta da aplicacao.
- **Just-in-time**: no comeco do marco que precisa, nao tudo upfront.
- Pasta por drill faz sentido aqui (drills sao isolados): `exercicios/NN-<conceito>/`.

## Roadmap vivo
A cada marco fechado, releia `PROGRESSO.md` e **recalibre os marcos restantes** (divida,
funda, ajuste granularidade) com base em como o aluno performou. O roadmap e uma espinha
estavel, mas as folhas adaptam.

## Marcos = git, nao pastas (para artefato unico)
Para um artefato unico que cresce (um app, um site), os marcos sao **estagios** marcados
com `git tag marco-NN-<slug>`, NAO pastas. `projeto/` tem UM conjunto de arquivos que
evolui marco a marco. Pastas-por-conceito existem apenas em `exercicios/` (drills isolados).

## Layout do repo do aluno
```text
<projeto>/
├── PROGRESSO.md          # fonte da verdade: perfil, DoD, marcos, dividas, log
├── exercicios/           # drills ISOLADOS, gerados just-in-time
│   └── NN-<conceito>/     #   pasta-por-conceito so aqui
└── projeto/              # o ARTEFATO UNICO; cresce marco a marco (marcos = git tags)
```

## Template — PROGRESSO.md
```markdown
# PROGRESSO — <nome do projeto>

## Perfil do aluno
- Ja sabe: ...
- Objetivo: ...
- Nivel atual: ...
- Restricoes (stack/tempo/ferramentas): ...

## Output final
<descricao do que sera construido>

## Definition of Done
- [ ] <criterio objetivo 1>
- [ ] <criterio objetivo 2>

## Marcos
- [ ] 00 — <meta>   <- ATUAL
- [ ] 01 — <meta>
- [ ] 02 — <meta>

## Dividas de aprendizado
- (registradas na curadoria; revisitar quando fizer sentido)

## Log
- AAAA-MM-DD — marco-00 fechado: <o que ficou pronto>
```

## Formato do scaffold (TODO human)
Cada arquivo entregue ao aluno em `projeto/` recebe, no topo, um comentario assim
(adapte a sintaxe de comentario a linguagem):
```text
/*
  MARCO NN — <nome>
  META: <o que vai ficar pronto>
  PORQUE: <que capacidade isso destrava no projeto>
  DONE: <como o aluno sabe que terminou>
  PERGUNTA-GUIA: <pergunta socratica que o aluno responde ANTES de codar>
*/
// TODO(human): <o que o aluno deve implementar aqui>
// PISTA (revele so se ele travar): <pista gradual, comentada>
```
NUNCA preencha o `TODO(human)`. O scaffold e o esqueleto; a carne e do aluno.
