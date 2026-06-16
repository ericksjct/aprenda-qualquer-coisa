# Auditoria de consistencia -- fechamento v1.0

**Data:** 2026-06-16
**Veredito:** PASS -- `sh scripts/check-consistencia.sh` => exit 0 (V-01..V-16 verdes).
**Escopo:** CONS-02 (anti cargo-cult: cada teoria de `fundamentos.md` aterrissa no doc citado)
e CONS-03 (anti-drift transversal: comandos, paths, conjunto de procedimentos, zero jargao
nos adaptadores). Este relatorio NAO edita `mentor/` nem o script -- so registra o estado
verde pos-Plano-02 (D-01 artefato b).

Este e o segundo e ultimo entregavel da fase, autorado APOS a suite ficar verde (Plano 02).
Cumpre tres papeis: (1) prova mecanica reproduzivel; (2) confirmacao semantica one-time do
CONS-02 (D-03, a unica verificacao manual da fase); (3) declaracao da politica de escalacao
(D-05) com o registro de quantos achados estruturais foram encontrados.

---

## Prova mecanica

Comando para reproduzir (da raiz do repo):

```sh
sh scripts/check-consistencia.sh; echo "exit=$?"
```

Saida literal capturada em 2026-06-16:

```
== CONS-02: anti-cargo-cult (cada teoria de fundamentos.md aterrissa no doc citado) ==
PASS  C2-backward-ref        in mentor/reference.md
PASS  C2-backward-novo       in mentor/novo-projeto.md
PASS  C2-align               in mentor/reference.md
PASS  C2-mayer               in mentor/reference.md
PASS  C2-expertrev           in mentor/reference.md
PASS  C2-retrieval           in mentor/tutor.md
PASS  C2-sdt                 in mentor/tutor.md
PASS  C2-mastery             in mentor/fecha-marco.md
PASS  C2-formativa           in mentor/metodo.md
PASS  C2-hattie              in mentor/debug.md
PASS  C2-spacing             in mentor/fecha-marco.md
== CONS-03 #1 (V-12): cada /comando tem mentor/<comando>.md (set fechado) ==
PASS  cmd-novo-projeto       mentor/novo-projeto.md
PASS  cmd-tutor              mentor/tutor.md
PASS  cmd-fecha-marco        mentor/fecha-marco.md
PASS  cmd-debug              mentor/debug.md
PASS  cmd-spidr-split        mentor/spidr-split.md
== CONS-03 #2 (V-13): paths em backticks resolvem (com SKIP de not-in-repo) ==
PASS  backtick-paths         =0
== CONS-03 #3 (V-14): zero jargao de metodo nos adaptadores (AGENTS.md + .claude/) ==
PASS  adapter-jargon         =0
== CONS-03 set-equality (V-15): conjunto de procedimentos -- DOIS LADOS por arquivo ==
PASS  set-eq AGENTS.md       5 canonicos presentes, 0 fora-do-set
PASS  set-eq README.md       5 canonicos presentes, 0 fora-do-set
PASS  set-eq mentor/metodo.md 5 canonicos presentes, 0 fora-do-set
== IN-01 (V-16): zero letras acentuadas em mentor/ ==
PASS  accents-mentor         =0
== 0 fail(s) ==
exit=0
```

`== 0 fail(s) ==` + `exit=0`: suite 100% verde. Este artefato reproduzivel substitui a
re-auditoria manual de 8 docs (D-03 rationale): re-auditar = rodar 1 comando (~0 tokens),
nao reler os docs.

### Mapeamento check -> V (contrato Nyquist 06-VALIDATION.md)

| Linha PASS no script | V | Requisito / SC |
|----------------------|---|----------------|
| `C2-backward-ref` ... `C2-spacing` (11 linhas) | V-01..V-11 | CONS-02 / SC1 -- cada ancora de teoria resolve no doc citado |
| `cmd-novo-projeto` ... `cmd-spidr-split` (5 linhas) | V-12 | CONS-03 / SC2 -- 5 comandos canonicos tem `mentor/<cmd>.md` |
| `backtick-paths =0` | V-13 | CONS-03 / SC2 -- paths em backtick resolvem (SKIP de not-in-repo) |
| `adapter-jargon =0` | V-14 | CONS-03 / SC4 -- zero jargao de metodo nos adaptadores |
| `set-eq AGENTS.md / README.md / metodo.md` (3 linhas) | V-15 | CONS-03 / SC3 -- igualdade de conjunto dos 5 procedimentos (DOIS lados) |
| `accents-mentor =0` | V-16 | IN-01 / D-07 -- zero letras acentuadas em `mentor/` |

16 criterios, 16 verdes. V-16 foi o unico red->green da fase (cedilhas de `debug.md:31-32`
removidas no Plano 02).

---

## CONS-02 -- confirmacao semantica (D-03, one-time)

O grep prova que a PALAVRA aparece; nao julga se a aplicacao faz SENTIDO. Esta e a unica
verificacao MANUAL da fase (06-VALIDATION.md "Manual-Only Verifications"). Para cada uma das
10 praticas com status flipado para `(aplicado)` em `fundamentos.md`, o agente ABRIU a linha
exata de aterrissagem (coluna "Exact landing line(s)" da CONS-02 Anchor Map em 06-RESEARCH.md)
e julgou o sentido. Veredito por pratica:

| # | Pratica | Doc:linha LIDA | Veredito |
|---|---------|----------------|----------|
| 1 | Backward Design | `reference.md:97-99` + `novo-projeto.md:56-60`,`:83-86` | Faz sentido. `reference.md:97` declara "ordem capacidade-primeiro, artefato-como-evidencia ... backward design: defina o resultado desejado (a capacidade) antes de desenhar a atividade"; `novo-projeto.md:56,58` chama o Passe-1->Passe-2 de "engenharia reversa do output final ... e o backward design". Genuina engenharia reversa do resultado, nao mencao incidental. |
| 2 | Constructive Alignment | `reference.md:76-77` (template `:85-87`) | Faz sentido. O template do CAMINHO co-loca `Objetivo (capacidade): ao terminar, voce consegue <verbo> <conceito>` (`:76`) imediatamente acima de `Entregavel: <o que o aluno ESCREVE> + <o que ele VE funcionando>` (`:77`). Objetivo<->Entregavel alinhados por construcao (META->DONE medindo o objetivo). |
| 3 | CLT / Mayer | `reference.md:350-354` | Faz sentido. "aplique os 3 principios de Mayer que transferem para texto -- coerencia ... sinalizacao ... segmentacao ... Os outros 9 tratam de audio/video e nao se aplicam". Sao exatamente os 3 que transferem para texto puro, com a ressalva honesta (anti-inflar o claim). |
| 4 | Worked-Example + Expertise-Reversal | `reference.md:33-34`,`:406`,`:416-418` | Faz sentido. `:406` titula a fase "eu faco -> nos fazemos -> voce faz"; `:416` define "eu faco" como worked example obrigatorio para zero-absoluto; `:33-34` nomeia o recuo do andaime como "expertise-reversal effect: suporte demais ATRAPALHA o avancado". GRR + recuo do andaime presentes. |
| 5 | Retrieval Practice | `tutor.md:37`,`:44` | Faz sentido. `:37` abre `## Passo 1 -- Recuperacao ativa (antes do recap)`; `:42` "o aluno responde de cabeca, SEM consultar a aula"; `:44` linka `retrieval practice`. A abertura pede recuperacao ativa ANTES de consultar a aula -- e retrieval, nao re-leitura. |
| 6 | SDT | `tutor.md:102-106` (espelho em `fecha-marco.md:126-129`) | Faz sentido. `:102` "Despeca com exatamente 1 proxima acao concreta"; `:103-104` ancora "em autonomia (voce escolheu este projeto) e competencia (voce ja VE o passo anterior funcionando)" + `:106` linka a ressalva honesta de relatedness em solo+IA. Proxima-acao-unica ancorada em autonomia/competencia, com a ressalva. |
| 7 | Mastery Learning | `fecha-marco.md:12`,`:15` | Faz sentido. `:12` titula `## Passo 1 -- Mastery gate: verificacao do "done"`; `:14-15` "so avanca apos dominio, nao so porque 'o codigo roda' (mastery learning)". E mastery gate por criterio de capacidade, nao gate de "roda". |
| 8 | Avaliacao Formativa | `metodo.md:77`,`:85` | Faz sentido. `:76-77` "antes de qualquer melhoria faca exatamente 1 pergunta de auto-explicacao: 'me explica por que isso funciona'"; `:85` "Guardrail: check formativo = exatamente 1 pergunta de auto-explicacao". Check formativo = 1 pergunta de auto-explicacao antes de avancar. |
| 9 | Feedback Hattie | `debug.md:16-18`,`:79` | Faz sentido. `:16-18` mapeia "feed-up (Aonde vou?) = Observar; feed-back (Como estou indo?) = Isolar+Hipoteses+Testar; feed-forward (Para onde a seguir?) = Corrigir+PISTA+Documentar"; `:79` "PISTA = feed-forward: aponta a direcao do proximo passo SEM entregar a resposta". As 3 lentes mapeadas; PISTA enquadrada como feed-forward que nao entrega a resposta. |
| 10 | Spacing Effect | `fecha-marco.md:73-78` | Faz sentido. `:73` "Agende a revisao espacada: na secao ## Agenda de retrieval do PROGRESSO.md, grave 1 entrada (load-bearing) do marco que acabou de fechar"; `:77` "o /tutor cobra essa entrada na abertura do proximo marco". Revisao espacada de marcos anteriores, agendada e cobrada -- e spacing real, nao so divida. |

**Resultado: 10/10 fazem sentido.** Cada termo grep-matcheado esta usado no sentido pretendido
da pratica (nao mencao incidental). Coerente com a previsao do RESEARCH (10/10, 0 estruturais).

---

## CONS-03 -- anti-drift

Os 4 checks transversais do CONS-03 (V-12..V-15) confirmados verdes pelo script:

- **V-12 -- comando <-> arquivo (set fechado):** os 5 comandos canonicos do roteamento de
  `AGENTS.md` (`novo-projeto`, `tutor`, `fecha-marco`, `debug`, `spidr-split`) tem cada um seu
  `mentor/<cmd>.md`. 5/5 PASS. Set FECHADO (allowlist), nao deteccao aberta de `/[a-z-]+` --
  evita falsos como `/config`, `/clear` (app-commands do Claude Code) e `/comando` (placeholder).
- **V-13 -- backtick-paths resolvem:** `backtick-paths =0` UNRESOLVED. Todo path repo-resident
  em backtick resolve; o SKIP regex isenta os not-in-repo intencionais (artefatos de runtime do
  aluno em `.projetos/<slug>/` -- `PROGRESSO.md`, `CAMINHO.md`, `APRENDIZADO.md`, `aulas/P0x-*`;
  placeholders `<slug>`/`<comando>`; `GEMINI.md`; formas relativas de link `reference.md`/`metodo.md`).
- **V-14 -- zero jargao nos adaptadores:** `adapter-jargon =0`. `AGENTS.md` + `.claude/` contem
  zero termos de metodo (SDT, mastery, backward design, Mayer, GRR, Hattie, feed-*, etc.). Os
  adaptadores so APONTAM para `mentor/` -- design fonte-unica preservado.
- **V-15 -- igualdade de conjunto (DOIS lados):** `AGENTS.md`, `README.md` e `mentor/metodo.md`
  cada um referencia os 5 canonicos (lado positivo, `faltando=0`) e nenhum `/comando` fora do
  set (lado negativo anti-drift, `fora-do-set=0`). 3/3 PASS. Fonte canonica do conjunto: tabela
  de roteamento de `AGENTS.md` (D-06).

---

## Correcoes aplicadas (D-05 trivial inline)

Politica D-05: o trivial e corrigido inline; o estrutural e escalado como achado. Os triviais
aplicados (no Plano 02, commit `086a82b`; aqui so registrados):

1. **IN-01 / D-07 -- acentos em `debug.md:31-32`:** `Peca`/`peca` (antes `Peca`/`peca` com
   cedilha) corrigidos inline. Eram as unicas letras acentuadas de `mentor/`. V-16 red->green;
   `mentor/` agora com `accents-mentor =0`.
2. **D-04 -- flip dos 10 status `pendente` -> `(aplicado)`:** as 10 marcas `(Fase N, pendente)`
   da coluna "Aplicado em" de `fundamentos.md` viraram `(aplicado)` apos a verificacao profunda
   (V-01..V-11) confirmar a aterrissagem. Zero `pendente` no arquivo; as 3 linhas `(ja presente)`
   (First Principles, CLT-core, ZPD) intactas. So virou "aplicado" o que D-03 confirmou de fato
   (ver tabela semantica acima).

---

## Achados estruturais escalados (D-05)

**Politica de escalacao (D-05):** seria achado ESTRUTURAL (apresentado, NAO fix silencioso):
teoria de `fundamentos.md` que NAO aterrissa em doc nenhum; metodo de fato duplicado num
adaptador (`.claude/`, `AGENTS.md`); divergencia real no conjunto de procedimentos entre
`AGENTS.md`/`README.md`/`metodo.md`. Triviais (flip de status, path quebrado, acento solto)
sao corrigidos inline (secao anterior); estruturais sao escalados.

**Registro: 0 achados estruturais.** Todas as 10 teorias aterrissam (10/10 fazem sentido,
tabela CONS-02 acima); zero jargao vazado para adaptadores (V-14 =0); conjunto de procedimentos
identico nos 3 arquivos (V-15 3/3). Nem o Plano 01 nem o Plano 02 escalaram nada -- os 11
anchors CONS-02 ja estavam verdes desde o Plano 01.

---

## Fora de escopo

- **FUT-04 -- verificador de drift COMPLETO (v2):** a Fase 6 entrega so o down-payment mecanico
  minimo (o que `grep`/teste-de-existencia consegue provar). O drift checker completo fica para v2.
- **Linter de acentos permanente (Risco #5, v2):** D-07 foi so o conserto pontual do IN-01. O
  check V-16 do harness enforca a convencao existente, mas NAO se expande para um linter de
  estilo permanente -- isso fica para v2.

---

Milestone v1.0 pronto para `/gsd-complete-milestone`: suite verde (exit 0), 10 confirmacoes
semanticas D-03, politica D-05 com 0 achados estruturais.
