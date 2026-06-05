---
name: spidr-split
description: Decompoe uma historia de usuario grande demais para um marco usando os 5 eixos do SPIDR Splitting. Use quando um marco parece grande, vago ou o aluno nao consegue articular o "done" em uma sessao.
---

# SPIDR Splitting — Decomposicao de Historias

Use esta skill quando uma historia de usuario (ou marco) parece grande demais para ser
completada numa sessao focada (~30-90 min), ou quando o aluno nao consegue articular
claramente o "done" do marco.

## Quando usar

- A historia tem mais de 1 capacidade coesa.
- O "done" envolve multiplos passos que o aluno nao consegue visualizar de uma vez.
- O marco estimado levaria mais de 90 minutos.
- Ha incerteza tecnica significativa ("nao sei por onde comecar").

## Os 5 eixos do SPIDR

Pergunte ao aluno (ou analise voce mesmo) cada eixo. Um ou mais eixos vao revelar
como quebrar a historia.

### S — Spike (Investigacao)

> "Ha alguma parte que voce nao sabe COMO fazer ainda?"

- Se sim: separe um **spike** — um marco de investigacao que reduz incerteza.
- O spike entrega CONHECIMENTO, nao codigo de producao.
- Exemplo: "Como a API de pagamento funciona?" -> spike de 1 sessao lendo docs + testando.

### P — Paths (Caminhos)

> "O usuario pode chegar ao resultado por caminhos diferentes?"

- Se sim: cada caminho feliz pode ser um marco separado.
- Exemplo: "login com email/senha" primeiro, "login com Google" depois.
- Comece pelo caminho mais simples (happy path).

### I — Interfaces (Superficies)

> "O mesmo recurso precisa aparecer em lugares diferentes?"

- Se sim: cada interface pode ser um marco.
- Exemplo: lista de tarefas na web (marco 1), lista de tarefas na API (marco 2).

### D — Data (Dados)

> "Ha variacoes de dados que complicam a implementacao?"

- Se sim: comece com dados simples, adicione complexidade depois.
- Exemplo: formulario basico (marco 1), formulario com upload de arquivo (marco 2).

### R — Rules (Regras)

> "Ha regras de negocio que podem ser adiadas?"

- Se sim: implemente a regra basica primeiro, regras avancadas depois.
- Exemplo: validacao de campo obrigatorio (marco 1), validacao customizada com regex
  e regras de dominio (marco 2).

## Processo

1. **Apresente a historia** que parece grande.
2. **Passe pelos 5 eixos** — pergunte ao aluno ou analise voce mesmo.
3. **Identifique os cortes** — quais eixos revelam divisoes naturais?
4. **Proponha as fatias** — cada uma com sua propria User Story, done e estimativa.
5. **Valide com o aluno** — "Essas fatias fazem sentido? Qual voce quer fazer primeiro?"
6. **Atualize o PROGRESSO.md** — substitua o marco grande pelas fatias.

## Exemplo

Historia original (grande):

```text
Como usuario, eu quero fazer checkout de um produto, para que eu possa compra-lo.
```

Aplicando SPIDR:

- **S**pike: "Como funciona a API de pagamento?" -> Marco 00-spike
- **P**aths: checkout com cartao (happy path) primeiro, boleto depois
- **R**ules: validacao basica de cartao primeiro, validacao completa + anti-fraude depois

Fatias resultantes:

```text
Marco 01 — Checkout basico (cartao, validacao simples)
  Como comprador, eu quero informar meus dados de cartao e ver a confirmacao,
  para que eu saiba que a compra foi registrada.

Marco 02 — Checkout com boleto
  Como comprador, eu quero escolher boleto como forma de pagamento,
  para que eu possa pagar sem cartao.

Marco 03 — Validacao avancada
  Como lojista, eu quero que o sistema valide cartoes com regras anti-fraude,
  para que eu evite chargebacks.
```

## Anti-padroes

- NAO quebre por tema tecnico ("primeiro o HTML, depois o CSS, depois o JS").
- NAO crie fatias que nao entregam valor sozinhas (cada uma deve ter um "done" claro).
- NAO esqueca de validar com o aluno antes de reescrever o PROGRESSO.md.
