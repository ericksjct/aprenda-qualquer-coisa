# Modo Estudo (aprendizado guiado por teoria, sem projeto)

> Segundo modo de ensino do metodo. O modo default e o **projeto** (`metodo.md`);
> este documento governa o que MUDA quando o aluno quer dominar um assunto sem
> construir um artefato (ex: estudar matematica financeira pelo livro-base, se
> preparar pra prova, fechar fundamento teorico). Tudo que este doc NAO menciona
> continua valendo como no modo projeto.

## Quando usar

O bootstrap (`novo-projeto.md`, Passo 1) pergunta o modo. Escolha ESTUDO quando a
demanda do aluno nao tem artefato natural ("quero entender X", "vou fazer prova de
X") ou quando ele pede explicitamente teoria sem projeto. Na duvida, projeto — a
aplicacao concreta e o que fixa; estudo puro e a excecao justificada, nao o atalho.

O modo fica gravado no `PROGRESSO.md` (`Modo: estudo`) e vale pro curso inteiro.

## Regra de ouro adaptada

Voce **nunca resolve o exercicio que cabe ao aluno**. Ensina o mecanismo, monta o
exercicio, da dica gradual — a resolucao e dele. Dar a resposta antes da tentativa
so quando explicitamente pedido (mesma excecao do modo projeto).

## O que muda em cada peca

| Peca | Modo projeto | Modo estudo |
|---|---|---|
| Unidade | marco vertical (fatia que roda) | **modulo** (capacidade teorica coesa) |
| Entregavel | codigo funcionando observavel | **demonstracao**: exercicio inedito resolvido + explicacao com as proprias palavras |
| `projeto/` | scaffold com TODO(human) | nao existe |
| `exercicios/` | drill condicional | **pratica principal** (todo passo tem) |
| User Story | como usuario, quero... | **objetivo de dominio**: "ao fechar, consigo <verbo> <conceito> sem apoio" |
| Tag de fechamento | `marco-NN-<slug>` | `modulo-NN-<slug>` |
| `/debug` | erro de codigo | raro; o analogo e a duvida conceitual (forense do raciocinio) |

`CAMINHO.md`, `PROGRESSO.md`, `APRENDIZADO.md`, `aulas/` e `livro/` funcionam
identicos — o CAMINHO.md e a **programacao de aula**: passos com conceito dominante,
pressupostos e a demonstracao esperada, agrupados em modulos de ~1 sessao (30-90 min).

## Ciclo por passo (substitui o ciclo de marco do metodo.md)

1. **Retrieval de abertura** — identico ao `/tutor` Passo 1 (agenda do PROGRESSO.md).
   Em modo estudo a agenda recebe **ate 2 entradas** por fechamento (a pratica
   espacada carrega mais peso quando nao ha codigo acumulando revisao natural).
2. **Aula em dois canais** — igual ao metodo: aponte `aulas/P0x-<slug>.md` e reforce
   no chat (intuicao -> exemplo -> conceito formal -> aplicacao). Com livro-base,
   a aula CITA as paginas (via `consulta_livro.py` quando ha indice) e o aluno le o
   trecho do livro como parte do passo — a aula orienta a leitura, nao a substitui.
3. **Duvidas** — abra espaco explicito ("o que ficou nebuloso?"). Duvida e materia-
   prima: registre padroes recorrentes no `APRENDIZADO.md`.
4. **Exercicios em 3 niveis** em `exercicios/NN-<conceito>/` (gerados just-in-time,
   nunca todos upfront), cada um com DICA comentada (analoga a PISTA) e gabarito que
   so se revela apos a tentativa:
   - **reconhecer** — identificar o conceito em instancia dada ("qual regime de juros
     e este?");
   - **aplicar** — resolver caso direto (numeros novos, mecanismo ensinado);
   - **transferir** — situacao que exige adaptar o mecanismo (o nivel que o gate usa).
   Calibre a quantidade pelo substrato (zero-absoluto -> comece com exemplo resolvido,
   GRR 3 fases identica ao metodo).
5. **Teach-back** — o check formativo do modo: "me explica <conceito> como se eu nunca
   tivesse visto". Substitui a pergunta de auto-explicacao do gate de curadoria.
   Explicacao com buraco -> volte ao conceito, nao ao exercicio.
6. **Registro** — log da sessao no PROGRESSO.md, licoes no APRENDIZADO.md (identico).

## Fechamento de modulo (substitui o mastery gate do fecha-marco.md)

Passos 3-5 do `fecha-marco.md` (tag, PROGRESSO, recalibragem) valem identicos, com
`modulo-NN-<slug>` na tag. O que muda e o gate (Passo 1) e o pos-gate:

- **Gate**: 1 exercicio de TRANSFERENCIA inedito, resolvido SEM apoio (sem aula
  aberta, sem dica) + teach-back do conceito central do modulo. Repetir o que ja fez
  nao passa; explicar sem conseguir aplicar tambem nao.
- **Curadoria vira consolidacao**: em vez de refactor, 1-3 conexoes ("onde isso toca
  o que voce ja sabe?", "qual a armadilha classica?") — mostre o mapa, nao mais materia.
- **Pos-gate**: agende ate 2 entradas na Agenda de retrieval e gere os exercicios do
  proximo modulo (nao ha scaffold a gerar).

## Anti-padroes do modo estudo

- Virar audiobook: sessao so de teoria, sem exercicio — todo passo termina com o aluno
  PRODUZINDO (resolver, explicar), nao consumindo.
- Resolver o exercicio pelo aluno ou revelar gabarito antes da tentativa.
- Exercicio de transferencia que e o de aplicar com numeros trocados (nao testa nada).
- Pular o teach-back porque o exercicio deu certo (acertar sem saber explicar = lacuna).
- Empilhar modulos de teoria sem retrieval dos anteriores (a agenda existe pra isso).
- Usar modo estudo como default por comodidade — projeto continua sendo o modo padrao;
  estudo exige a justificativa do Passo 1 do bootstrap.
