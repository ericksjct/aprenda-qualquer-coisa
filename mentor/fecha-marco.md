# Fechamento de Marco

Fecha um marco de aprendizado de forma sistematica e prepara o terreno para o proximo.
Use quando o aluno diz "terminei", "funcionou" ou quando voce avalia que o criterio de
"done" foi atingido.

## Pre-requisitos

- O codigo do marco atual funciona (make it work).
- O aluno entende o que construiu (consegue explicar).

## Passo 1 — Verificacao do "done"

Confirme com o aluno (ou verifique voce mesmo) cada criterio de "done" do marco atual:

- [ ] O codigo executa/renderiza sem erros?
- [ ] O aluno consegue explicar o que cada parte faz?
- [ ] A User Story do marco esta satisfeita?

Se algum criterio falhar, o marco NAO esta fechado. Volte ao ciclo de ensino.

## Passo 2 — Curadoria (make it right)

Agora que funciona, ofereca **1 a 3 melhorias** ordenadas por impacto:

1. **Legibilidade** — nomes, organizacao, comentarios utilitarios.
2. **Idiomatico** — padroes da linguagem/framework que o aluno ainda nao conhece.
3. **Robustez** — tratamento de erro, edge cases, validacoes.

Para cada melhoria:
- Explique **por que** melhora (o principio por tras).
- Mostre **como** fica (exemplo de codigo).
- Deixe o aluno **decidir** se aplica agora ou registra como divida.

Se o aluno optar por nao refatorar agora, registre no `PROGRESSO.md` como divida de
aprendizado.

## Passo 3 — Git tag

Crie uma tag para marcar o ponto de chegada. Rode dentro do repo do projeto
(`.projetos/<slug>/`, que tem seu proprio `git init` — ver `mentor/reference.md`):

```text
git add .
git commit -m "marco-NN-<slug>: <resumo do que foi entregue>"
git tag marco-NN-<slug>
```

Explique ao aluno: "Essa tag e um checkpoint. Voce pode voltar aqui se precisar."

## Passo 4 — Atualizar PROGRESSO.md

Atualize o arquivo com:

1. Marque o marco atual como fechado (`- [x]`).
2. Atualize o marco atual para o proximo (`<- ATUAL`).
3. Adicione ao **Log**: data, marco fechado, o que ficou pronto.
4. Transfira **dividas de aprendizado** da curadoria (se houver).
5. Atualize a **tabela de substrato**: o aluno exercitou assuntos neste marco —
   se a performance mostrou subida (ou descida) de nivel, registre com a evidencia.

## Passo 5 — Recalibrar CAMINHO.md e marcos restantes

Releia o `CAMINHO.md` (passos restantes + mapa passos -> marcos) e o `PROGRESSO.md`,
e ajuste conforme necessario:

- **Divida** um marco que agora parece grande demais (use `/spidr-split`).
- **Funda** marcos muito pequenos que podem ser combinados.
- **Ajuste a ordem** se o aprendizado do marco atual revelou dependencias novas —
  isso inclui **inserir passos** no `CAMINHO.md` quando um buraco de conceito apareceu.
- **Atualize User Stories** se o entendimento do projeto evoluiu.
- Re-rode a **verificacao de coesao** (checklist em `mentor/reference.md`):
  nenhum passo restante pode pressupor conceito nao introduzido nem coberto pelo
  substrato atualizado.

Pergunte ao aluno: "Agora que voce viu isso funcionando, os proximos marcos ainda fazem
sentido na ordem atual?"

## Passo 6 — Scaffold do proximo marco

Gere o scaffold do proximo marco em `projeto/`, seguindo os passos correspondentes
do `CAMINHO.md` e o formato completo de `mentor/reference.md`:

- Arquivos com cabecalho completo (META, PORQUE, PRESSUPOE, ARQUIVOS,
  EXEMPLO-DE-RESULTADO, DONE, PERGUNTA-GUIA) + `TODO(human)` descrevendo
  comportamento observavel + PISTA comentada.
- Valide o `PRESSUPOE` contra os passos ja fechados do `CAMINHO.md` e a tabela de
  substrato atualizada. Assunto zero-absoluto -> "eu faco -> voce faz".
- Se a regra de drill disparar, gere drill em `exercicios/`.
- Lembre o aluno de que o proximo marco comeca agora — e que a proxima sessao de
  estudo abre com `/tutor`.

## Checkpoint final

Antes de entregar o scaffold, confirme:

- [ ] PROGRESSO.md atualizado (incluindo tabela de substrato).
- [ ] CAMINHO.md recalibrado e coeso (verificacao de coesao passou).
- [ ] Git tag criada.
- [ ] Proximo marco tem User Story clara e entregavel observavel.
- [ ] Scaffold gerado no formato completo, com PRESSUPOE validado.
- [ ] Aluno sabe qual e o proximo passo.

## Anti-padroes

- NAO pule a curadoria (e onde o aluno aprende a "fazer direito").
- NAO esqueca de criar a git tag (e o historico de progresso).
- NAO avance para o proximo marco sem atualizar o PROGRESSO.md.
- NAO recalibre sozinho — envolva o aluno na decisao de ajustar o roadmap.
