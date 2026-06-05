# Migracao GSD — O que mudou

> Comparativo entre a versao anterior (`e9445f3`) e a versao com filosofias GSD (`55f0e38`).

---

## Resumo executivo

| Aspecto | Antes | Depois |
|---|---|---|
| **Skills** | 2 (bootstrap PT + EN) | 4 (+ spidr-split, fecha-marco, debug) |
| **Arquivos alterados** | — | 6 modificados + 3 novos |
| **Insercoes/remocoes** | — | +755 / -51 |
| **Filosofia central** | Marcos verticais, TODO human | Marcos verticais + **Demanda-First, User Story, Walking Skeleton, Forense, SPIDR, Substrato** |

---

## 1. Output Style (`mentor-projeto.md`)

### Antes
- Erro = depuracao do pensamento: apontar erro, explicar, corrigir.
- Fechamento de marco: tag + PROGRESSO.md + proximo.
- Anti-padroes: 7 itens.

### Depois

#### Novo: Protocolo de forense (6 passos)

```text
1. Observar: "O que voce esperava? O que aconteceu de fato?"
2. Isolar: "Qual e a menor parte do codigo que reproduz o problema?"
3. Hipoteses: "O que poderia estar causando? Liste 2-3 possibilidades."
4. Testar: "Como verificar qual hipotese esta certa?"
5. Corrigir: Aplique e verifique.
6. Documentar: Registre no APRENDIZADO.md.
```

> **Impacto:** O erro deixa de ser "apontar e corrigir" e vira **investigacao sistematica**
> que ensina o aluno a debugar sozinho no futuro.

#### Novo: User Story por marco

```text
Como [tipo de usuario], eu quero [capacidade], para que [beneficio].
```

> **Impacto:** Cada marco ganha um "norte" de valor. Se o aluno nao articula o "para que",
> o marco esta mal definido.

#### Novo: Substrato por assunto (correcao de aluno)

> Distinga **nivel global** de **substrato por assunto**. O aluno pode ser avancado num
> dominio (ex: logica/dados) e zero-absoluto noutro (ex: sintaxe de frontend). Zero-absoluto
> NAO e o mesmo que iniciante — zero nao deduz uma sintaxe que nunca viu.

> **Impacto:** Evita que o aluno zero-absoluto num assunto caia em abismo de "descobrir
> sozinho" sem materia-prima pra raciocinar.

#### Novo: Referencia ao SPIDR Splitting

> Quando uma historia for grande demais, use `/spidr-split`.

#### Novo: Referencia ao fechamento sistematico

> Para fechamento sistematico, use `/fecha-marco`.

#### Novo: Anti-padroes (4 itens de substrato)

- Fazer pergunta-guia sobre sintaxe que o aluno nunca viu (descoberta sem chao = abismo).
- Deixar a PISTA virar a unica ponte de avanco (forca copia cega em vez de entendimento).
- Tratar zero-absoluto num assunto como se fosse iniciante (andaime curto demais).
- Entregar o scaffold sem explicar, na 1a vez, a ordem de leitura dos campos.

---

## 2. Skill de Bootstrap (`novo-projeto/SKILL.md`)

### Antes (5 passos)

```
Passo 1 — Diagnostico
Passo 2 — Roadmap
Passo 3 — Aprovacao
Passo 4 — Esqueleto
Passo 5 — Scaffold do Marco 00
```

### Depois (6 passos)

```
Passo 1 — Diagnostico (+ substrato por assunto)
Passo 2 — Roadmap
Passo 3 — User Stories (uma por marco)        <- NOVO
Passo 4 — Aprovacao (Demanda-First)           <- renumerado + reforcado
Passo 5 — Esqueleto (+ APRENDIZADO.md)        <- renumerado + novo arquivo
Passo 6 — Walking Skeleton (Marco 00)         <- renumerado + nova filosofia
```

#### Passo 1 — Diagnostico (novo bullet de substrato)

- Mapeie o **substrato por assunto**, nao so o nivel global: para cada assunto que a stack
  do projeto exige (ex: HTML, CSS, JS), o aluno e avancado, iniciante ou zero-absoluto?
  Zero-absoluto num assunto muda o andaime (exige "eu faco -> voce faz", nao pergunta
  socratica seca).

> **Impacto:** O diagnostico agora captura zero-absoluto por assunto, nao so nivel medio.

#### Passo 3 — User Stories (NOVO)

- Cada marco enquadrado como historia de usuario.
- "Como" = quem usa, "quero" = capacidade, "para que" = valor/done.
- Se grande demais, usa SPIDR Splitting antes de prosseguir.

> **Impacto:** Marcos deixam de ser "meta tecnica" e viram "entrega de valor".

#### Passo 4 — Aprovacao (reforcado)

- Adicionado: "apresente as User Stories de cada marco".
- Adicionado: regra **Demanda-First** — nenhum codigo antes da demanda clara e aprovada.

> **Impacto:** O aluno valida o entendimento antes de qualquer arquivo ser criado.

#### Passo 5 — Esqueleto (novo arquivo)

- Adicionado: `APRENDIZADO.md` (vazio, pronto para preencher).
- Conteudo: diario de licoes, padroes de erro, decisoes arquiteturais.

> **Impacto:** O aluno constroi um "dicionario de erros" pessoal ao longo do projeto.

#### Passo 6 — Walking Skeleton (nova filosofia + calibragem de substrato)

- Marco 00 deixa de ser "scaffold generico" e vira **esqueleto ambulante**.
- Prova que todas as camadas funcionam juntas (HTML+CSS+JS, rota+JSON, tela+nav, etc.).
- NAO implementa logica de negocio — so prova que o pipeline "respira".
- **Novo:** Calibre o scaffold ao **substrato**: se exige sintaxe nunca vista, use
  "eu faco -> voce faz" (exemplo resolvido + variacao) em vez de pergunta-guia seca.
- **Novo:** Na 1a entrega, explique a ordem de leitura dos campos do scaffold
  (META -> PORQUE -> PERGUNTA-GUIA -> TODO -> DONE -> PISTA).

> **Impacto:** O aluno ganha confianca no dia 1 vendo o projeto funcionar end-to-end,
> e nao cai em abismo quando zero-absoluto num assunto.

---

## 3. Reference (`novo-projeto/reference.md`)

### Antes
- Regra de granularidade
- Marcos verticais
- Drill condicional
- Roadmap vivo
- Marcos = git
- Layout do repo
- Template PROGRESSO.md
- Formato do scaffold

### Depois (tudo acima +)

#### Novo: Substrato por assunto (na regra de granularidade)

> **Substrato por assunto, nao por aluno**: o nivel GLOBAL engana. Um aluno pode ser
> avancado em logica/dados e ZERO-ABSOLUTO na sintaxe de um assunto novo. Calibre pelo
> substrato DO ASSUNTO em jogo, nao por uma media do aluno.

#### Novo: User Story por marco

- Formato canonico: `Como [usuario], eu quero [capacidade], para que [beneficio].`
- A historia e o "norte" do marco.
- Se "para que" nao e claro, use `/spidr-split`.

#### Novo: SPIDR Splitting

Cinco eixos de decomposicao:

| Eixo | Pergunta | Exemplo |
|---|---|---|
| **S**pike | Ha parte que nao sabemos COMO fazer? | "Como funciona a API X?" |
| **P**aths | Ha caminhos alternativos? | Cartao vs boleto |
| **I**nterfaces | Precisa aparecer em lugares diferentes? | Web vs mobile vs API |
| **D**ata | Ha variacoes de dados? | Form simples vs com upload |
| **R**ules | Ha regras adiaveis? | Validacao basica vs completa |

> **Impacto:** Ferramenta concreta para quebrar marcos grandes em fatias viaveis.

#### Novo: Como o aluno le o scaffold (explique na 1a entrega)

Os campos sao uma SEQUENCIA, nao um menu pra escolher "qual seguir":

```text
META -> onde voce quer chegar (o destino)
PORQUE -> por que isso importa (motivacao)
PERGUNTA-GUIA -> PENSE antes de digitar (constroi o entendimento)
TODO(human) -> o que voce DIGITA (a unica acao a executar)
DONE -> como saber que acertou (o teste final)
PISTA -> rede de seguranca, so se travar de vez
```

> **Impacto:** O aluno nao trava sem saber qual campo executar.

#### Novo: Sintaxe nova de verdade — "eu faco -> voce faz"

> Descoberta socratica so funciona quando o aluno tem materia-prima pra raciocinar. Se o
> TODO exige sintaxe NUNCA vista (zero-absoluto), a pergunta-guia vira abismo e a PISTA
> acaba sendo a unica saida — forca copia cega, nao aprendizado.

> Nesse caso, inverta: MOSTRE um exemplo resolvido primeiro (o "eu faco"), explique cada
> pedaco, e so entao peca APLICACAO numa VARIACAO (o "voce faz"). Isso prova entendimento
> sem ser copia.

> **Impacto:** Zero-absoluto ganha chao pra aprender em vez de cair em abismo.

#### Novo: Template APRENDIZADO.md

```markdown
# Diario de Aprendizado

## Licoes
- AAAA-MM-DD — <conceito> (contexto: <marco>)

## Padroes de erro
- AAAA-MM-DD — <erro> -> <causa> -> <como evitar>

## Decisoes arquiteturais
- AAAA-MM-DD — <decisao> (contexto: <por que>)

## Dividas de aprendizado
- <divida> — <data> — revisitar no marco <NN>
```

> **Impacto:** Documentacao ativa do aprendizado, nao so do codigo.

#### Novo: Protocolo de forense

- Os 6 passos documentados para referencia rapida.

#### Novo: Walking Skeleton

- Definicao + exemplos por tipo de projeto (web, backend, mobile, CLI, data/ML).

#### Template PROGRESSO.md atualizado

- Marcos agora incluem **User Story**.
- Marco 00 explicitamente rotulado como "(Walking Skeleton)".

#### Layout do repo atualizado

```text
Antes:                    Depois:
<projeto>/                <projeto>/
├── PROGRESSO.md          ├── PROGRESSO.md
├── exercicios/           ├── APRENDIZADO.md      <- NOVO
└── projeto/              ├── exercicios/
                          └── projeto/
```

---

## 4. README.md

### Antes
- Bilingue (PT + EN).
- 2 componentes base + skills auxiliares.
- 8 principios.
- Layout com 5 skills (incluindo new-project EN).

### Depois
- **Apenas PT-BR.** Ingles removido.
- 1 output style + 4 skills.
- **9 principios** (1 novo: Substrato por assunto).
- Instrucoes de uso das skills auxiliares.
- Layout com 4 skills (apenas PT).

#### Novo principio

```text
- Substrato por assunto, nao por aluno. Zero-absoluto num assunto nao e o mesmo que
  iniciante. Descoberta socratica so funciona com materia-prima pra raciocinar.
```

---

## 5. Novas Skills (3 arquivos novos)

### `/spidr-split` — Decomposicao de historias

- Quando usar: marco grande, vago, "done" nao claro.
- Os 5 eixos com perguntas-guia e exemplos.
- Processo de 6 passos (apresentar -> 5 eixos -> identificar cortes -> propor fatias -> validar -> atualizar PROGRESSO.md).
- Exemplo completo: checkout de produto decomposto em 3 marcos.
- Anti-padroes: nao quebrar por tema, nao criar fatias sem valor, nao esquecer validacao.

### `/fecha-marco` — Fechamento sistematico

- 6 passos: verificacao do done -> curadoria -> git tag -> PROGRESSO.md -> recalibrar -> scaffold do proximo.
- Curadoria: 1-3 melhorias (legibilidade, idiomatico, robustez).
- Recalibracao: dividir, fundar, reordenar, atualizar User Stories.
- Checkpoint final com 5 checks.
- Anti-padroes: nao pular curadoria, nao esquecer tag, nao recalibrar sozinho.

### `/debug` — Protocolo de forense

- 6 passos do protocolo com perguntas exatas.
- Variacoes: sintaxe, logica, conceito, ambiente.
- Dicas de ensino: nunca "voce errou", elogie o processo, deixe o aluno falar.
- Anti-padroes: nao dar resposta no passo 1, nao pular passos, nao deixar de documentar.

---

## Mapa de impacto

```text
Fluxo anterior:
  Demanda -> Roadmap -> Scaffold -> Codigo -> Done -> Proximo

Fluxo GSD:
  Demanda -> Diagnostico (+ substrato por assunto)
    -> Roadmap -> User Stories -> Aprovacao (Demanda-First)
    -> Walking Skeleton (Marco 00, calibrado ao substrato)
    -> Codigo -> Erro (Forense 6 passos)
    -> Done -> Curadoria -> Git tag -> APRENDIZADO.md -> Recalibrar
    -> /spidr-split (se proximo marco grande) -> Proximo
```

---

## Estatisticas

| Metrica | Valor |
|---|---|
| Arquivos modificados | 6 |
| Arquivos criados | 3 |
| Arquivos removidos | 2 (versao EN) |
| Linhas adicionadas | 755 |
| Linhas removidas | 51 |
| Skills totais | 4 |
| Novos conceitos | 7 (Demanda-First, User Story, Walking Skeleton, SPIDR, Forense, APRENDIZADO.md, Substrato) |
