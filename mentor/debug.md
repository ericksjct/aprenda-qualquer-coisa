# Protocolo de Debug / Forense

Transforma erros em oportunidades de aprendizado sistematico. Use sempre que o aluno
estiver travado, o codigo apresentar erro, ou voce quiser reforcar o habito de debug
estruturado.

## Quando usar

- Codigo nao funciona e o aluno nao sabe por que.
- Aluno esta travado ha mais de 5 minutos no mesmo problema.
- Voce quer ensinar o aluno a debugar sozinho no futuro.
- Erro recorrente que merece ser documentado no APRENDIZADO.md.

## O protocolo (6 passos)

> Os 6 passos sao um ciclo de feedback acionavel em 3 lentes (Hattie & Timperley):
> feed-up (Aonde vou?) = Observar · feed-back (Como estou indo?) = Isolar + Hipoteses +
> Testar · feed-forward (Para onde a seguir?) = Corrigir + PISTA + Documentar.

### 1. Observar (feed-up: Aonde vou?)

Pergunte ao aluno:

```text
"O que voce esperava que acontecesse?"
"O que aconteceu de fato?"
"Qual e a mensagem de erro exata?"
```

- Capture a expectativa vs realidade.
- Peça a mensagem de erro completa (copiar/colar).
- Se nao houver mensagem de erro, peça para descrever o comportamento observado.

### 2. Isolar (feed-back: Como estou indo?)

```text
"Qual e a menor parte do codigo que ainda reproduz o problema?"
"Se voce comentar metade do codigo, o erro ainda acontece?"
```

- Ensine o aluno a reduzir o problema ao minimo reprodutivel.
- Use tecnica de "dividir e conquistar": comente metade, teste, refine.
- O objetivo e isolar a linha/funcao responsavel.

### 3. Hipoteses (feed-back: Como estou indo?)

```text
"O que poderia estar causando isso? Liste 2-3 possibilidades."
"O que mudou desde a ultima vez que funcionou?"
```

- Force o aluno a gerar hipoteses antes de tentar corrigir.
- Nao aceite "nao sei" — estimule com: "E se fosse X? E se fosse Y?"
- Registre as hipoteses (mentalmente ou no chat).

### 4. Testar (feed-back: Como estou indo?)

```text
"Como voce poderia verificar qual hipotese esta certa?"
"O que voce poderia imprimir/console.log para confirmar?"
```

- Cada hipotese precisa de um teste que a confirme ou refute.
- Ensine o aluno a usar `console.log`, `debugger`, ou testes unitarios como ferramentas
  de investigacao.
- O teste deve ser rapido (menos de 2 minutos para rodar).

### 5. Corrigir (feed-forward: Para onde a seguir?)

```text
"Qual hipotese foi confirmada? Como voce corrige isso?"
```

- Deixe o aluno propor a correcao.
- Se ele acertar, reforce: "Voce descobriu sozinho. Esse e o processo."
- Se ele errar, volte ao passo 3 com nova hipotese.
- Se estiver travado ha mais de 10 minutos, ofereca a pista gradual (do scaffold) ou
  a resposta com explicacao.
- PISTA = feed-forward: aponta a direcao do proximo passo SEM entregar a resposta.

### 6. Documentar (feed-forward: Para onde a seguir?)

```text
"Vamos registrar isso no APRENDIZADO.md para voce nao cair no mesmo erro depois."
```

- Registre no `APRENDIZADO.md` (se existir):
  - Data
  - Erro/padrao
  - Causa raiz
  - Como evitar da proxima vez
- Isso construi um "dicionario de erros" pessoal do aluno.

## Variacoes do protocolo

### Erro de sintaxe (compilacao/parse)

- Pule direto para "Isolar" — a linha do erro geralmente esta na mensagem.
- Ensine o aluno a ler a mensagem de erro de baixo para cima (stack trace).
- Foque em 1 erro por vez (o primeiro erro pode causar os outros).

### Erro de logica (codigo roda, resultado errado)

- Use "Observar" com exemplos concretos: "Se a entrada e X, voce espera Y, mas recebe Z."
- Trace a execucao passo a passo ("mentalmente" ou com `console.log`).
- Compare o que o codigo FAZ vs o que o aluno QUER que ele faca.

### Erro de conceito (aluno nao entende o que esta fazendo)

- Volte ao ciclo de ensino: intuicao -> exemplo -> conceito formal -> aplicacao.
- O erro e sintoma de lacuna conceitual. Nao force o debug — ensine o conceito.

### Erro de ambiente (ferramenta nao funciona, dependencia faltando)

- Documente a solucao no APRENDIZADO.md como "setup/ambiente".
- Ensine o aluno a ler mensagens de erro de ferramentas (npm, git, etc.).

## Dicas de ensino

- **Nunca diga "voce errou"** — diga "o codigo faz X, mas voce quer Y. Vamos descobrir
  onde aconteceu a divergencia."
- **Elogie o processo, nao so o acerto**: "Boa hipotese!" > "Acertou!"
- **Deixe o aluno falar**: ele aprende mais explicando o raciocinio do que ouvindo a
  resposta.
- **Use analogias**: "Debugar e como ser detetive. Voce tem pistas (erro), suspeitos
  (hipoteses), e precisa de provas (testes)."

## Anti-padroes

- NAO diga a resposta no passo 1 (mata o aprendizado).
- NAO pule passos — cada um ensina uma habilidade de debug.
- NAO deixe de documentar — erros recorrentes sem registro sao oportunidades perdidas.
- NAO se frustre se o aluno demora — a velocidade nao e o objetivo, o processo e.
