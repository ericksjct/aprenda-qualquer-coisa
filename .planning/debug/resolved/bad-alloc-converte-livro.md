---
status: resolved
trigger: "Flood de std::bad_alloc em scripts/converte_livro.py ao converter livros didaticos grandes. O script faz UMA conversao do documento inteiro (converter.convert(pdf_path) em convert_pdf, ~linha 196), diferente do script de referencia C:\\Users\\Erick\\Documents\\Projetos\\docling-extrair-pdf\\converter.py que evita bad_alloc fazendo chunking pagina-por-pagina (PdfWriter por pagina + docling.convert por pagina + gc.collect() apos cada pagina). O fallback de page_range em lotes esta documentado mas NAO implementado (linhas 193-195). Objetivo: reintroduzir a estrategia de chunking/incremental do converter.py de referencia, mantendo o split deterministico por capitulo, ancoras de pagina e slug safety. Criar/ajustar testes (tests/test_converte_livro.py) e garantir que rode perfeitamente."
created: 2026-06-22
updated: 2026-06-22T20:57:00Z
---

# Debug Session: bad-alloc-converte-livro

## Symptoms

- **Expected behavior:** `scripts/converte_livro.py` converte um PDF de livro didatico grande
  em markdown por capitulo (com ancoras de pagina) sem crash, rodando local ate o fim.
- **Actual behavior:** Flood de `std::bad_alloc` durante a conversao; o pipeline do docling
  estoura memoria.
- **Error messages:** `std::bad_alloc` (falha de alocacao C++ vinda do pipeline docling/OCR).
- **Timeline:** Surgiu na implementacao da Fase 7, quando o script passou a fazer UMA
  conversao do documento inteiro em vez do chunking pagina-por-pagina do script de referencia.
- **Reproduction:** Rodar `python scripts/converte_livro.py <pdf-grande> --slug <slug>` num
  livro didatico grande aciona o flood de bad_alloc.

## Initial Diagnosis (do usuario)

- Causa provavel: `convert_pdf()` chama `converter.convert(pdf_path)` sobre o PDF inteiro
  (`scripts/converte_livro.py:196`), segurando o documento todo na memoria.
- Script de referencia `converter.py` evita o problema com chunking pagina-por-pagina:
  `PdfReader`/`PdfWriter` extrai 1 pagina -> `docling.convert` nessa pagina -> append no md ->
  `gc.collect()` a cada ciclo.
- O fallback de `page_range` em lotes esta apenas DOCUMENTADO (linhas 193-195), nunca implementado.

## Objetivo da correcao

Reintroduzir a estrategia incremental/chunked do `converter.py` de referencia, PRESERVANDO:
- split deterministico por capitulo (`split_into_chapters`)
- ancoras `<!-- page: N -->` (`render_chapter`)
- slug safety / path-safety (`sanitize_slug`)
- `markdownlint --fix` por arquivo
E criar/ajustar testes em `tests/test_converte_livro.py` para cobrir o caminho chunked
sem exigir docling (helpers puros + monkeypatch).

## Evidence

- timestamp: 2026-06-22T00:00:00Z
  checked: scripts/converte_livro.py convert_pdf() linha 196 vs converter.py de referencia
  found: convert_pdf() chama `converter.convert(pdf_path)` UMA vez sobre o PDF inteiro; o
    fallback de page_range em lotes esta apenas comentado (linhas 193-195), nunca implementado.
  implication: confirma a causa-raiz suspeita pelo usuario - nao ha chunking real no caminho feliz.

- timestamp: 2026-06-22T00:05:00Z
  checked: `inspect.signature(DocumentConverter.convert)` no venv .venv-pdf (docling instalado)
  found: `convert()` aceita `page_range: Tuple[int,int] = (1, sys.maxsize)` nativamente; nao
    precisa de PdfWriter/temp-PDF como a referencia faz.
  implication: existe um mecanismo built-in do docling para converter em lotes sem precisar
    fatiar o PDF manualmente.

- timestamp: 2026-06-22T00:10:00Z
  checked: docling/pipeline/base_pipeline.py:239-254 (_build_document) e
    docling/backend/docling_parse_backend.py
  found: `self.page_count = self._backend.page_count()` usa o backend aberto sobre o PDF
    ORIGINAL completo (nao um arquivo de 1 pagina); em `_build_document`, o loop
    `for i in range(conv_res.input.page_count): ... conv_res.pages.append(Page(page_no=i+1))`
    SO inclui paginas dentro de `page_range`, mas `page_no` usa o indice ABSOLUTO `i+1` do
    documento completo - nao reseta para 1 a cada lote.
  implication: `page_range=(s,e)` em lotes preserva os numeros de pagina NATIVOS/verdadeiros,
    ao contrario do approach da referencia (PdfWriter por pagina), que cria um PDF de 1 pagina
    isolado e por isso SEMPRE reporta page_no=1 internamente. page_range e estritamente melhor
    para este caso de uso porque converte_livro.py DEPENDE de page_no real para as ancoras
    `<!-- page: N -->` e para `_page_of()`/`split_into_chapters`.

- timestamp: 2026-06-22T00:12:00Z
  checked: requirements-pdf.txt e pypdf instalado no .venv-pdf
  found: pypdf>=4.0 ja e dependencia declarada (mesma do PdfReader da referencia); pode ser
    usado via import lazy (mesmo padrao de docling) so para contar paginas totais do PDF antes
    de gerar os lotes de page_range.
  implication: nao precisa de nova dependencia; só import lazy de PdfReader dentro de
    convert_pdf (ou helper auxiliar) para `len(PdfReader(pdf_path).pages)`.

- timestamp: 2026-06-22T00:14:00Z
  checked: `split_into_chapters` / `synthetic_doc` fixture (tests/conftest.py) - como consomem
    `doc.iterate_items()`
  found: o unico metodo usado de `doc` e `iterate_items()`, que so precisa yield-ar tuplas
    `(item, level)`. O item so precisa expor `.label.name`, `.level`, `.text`, `.prov[0].page_no`
    (duck typing, ja confirmado pelo SyntheticDoc de teste).
  implication: para mesclar N resultados de `convert()` em lotes, NAO e necessario mesclar
    objetos DoclingDocument internamente (frágil/nao documentado); basta um wrapper leve que
    encadeia `iterate_items()` de cada `result.document` de cada lote, em ordem. Isso reusa o
    mesmo contrato duck-typed que os testes ja validam.

- timestamp: 2026-06-22T20:57:00Z
  checked: VERIFICACAO HUMANA FINAL - usuario rodou a versao corrigida sobre o PDF de livro
    grande REAL que originalmente estourava com flood de std::bad_alloc.
  found: o pipeline processou multiplas paginas via RapidOCR por ~4 minutos (20:53 -> 20:57+)
    e chegou ao final ("OK") SEM nenhum std::bad_alloc. O batching por page_range segura a
    memoria. Os avisos "RapidOCR returned empty result" / "text detection result is empty" sao
    BENIGNOS (paginas sem texto detectavel por OCR - ex. paginas so-imagem/em branco), nao erros.
  implication: causa-raiz confirmada e fix validado em producao real. O flood de bad_alloc foi
    ELIMINADO no livro grande real, nao apenas em fixtures sinteticas. VEREDITO DO USUARIO:
    CONFIRMADO FIXED.

## Eliminated

- hypothesis: Resetar `page_no` a cada lote (como a referencia faz, 1 pagina por vez) e
    aceitavel desde que se ajuste a logica de ancora.
  evidence: converte_livro.py exige page_no VERDADEIRO/nativo para `<!-- page: N -->` e para
    a navegacao operador->livro; resetar quebraria essa garantia (D-10). page_range resolve
    isso sem nenhum trade-off, entao essa hipotese-caminho foi descartada antes de ser tentada.
  timestamp: 2026-06-22T00:15:00Z

## Current Focus

- hypothesis: CONFIRMADO (ver Resolution). Empiricamente validado com docling real
  (.venv-pdf) sobre tests/fixtures/sample.pdf (2 paginas) com batch_size=1: os
  page_no observados nos itens foram [1, 2] - ou seja, page_range preserva o
  numero de pagina VERDADEIRO mesmo em lotes, ao contrario do approach de
  temp-PDF de 1 pagina (que sempre reportaria page_no=1).
- test: golden smoke (test_golden_smoke, marcado @pytest.mark.slow) + script
  ad-hoc rodado com .venv-pdf/Scripts/python.exe chamando convert_pdf(...,
  batch_size=1) diretamente sobre o sample.pdf real.
- expecting: page_no sequencial e crescente atraves dos lotes (nao resetando
  para 1 a cada lote).
- next_action: RESOLVIDO. Usuario confirmou FIXED no livro grande real (sem bad_alloc,
  run de ~4 min completou OK). Sessao movida para resolved/ e fix commitado.
- reasoning_checkpoint:
  hypothesis: "convert_pdf() faz UMA conversao do documento inteiro via converter.convert(pdf_path), o que forca o pipeline docling/OCR a manter o documento inteiro (paginas+buffers OCR+imagens) na memoria simultaneamente; isso causa std::bad_alloc em livros grandes. O fix correto e converter em lotes de N paginas via `page_range=(s,e)` nativo do docling (sem PdfWriter/temp PDFs), encadeando iterate_items() de cada lote e chamando gc.collect() entre lotes, preservando page_no verdadeiro (confirmado: page_range NAO reseta page_no, ao contrario de temp-PDFs de 1 pagina)."
  confirming_evidence:
    - "Linha 196 de converte_livro.py faz converter.convert(pdf_path) sem nenhum page_range/limite - unico ponto de conversao no caminho feliz (linhas 193-195 documentam o fallback em comentario, nunca implementado)."
    - "docling/pipeline/base_pipeline.py:251-254 prova que page_range filtra paginas processadas mas Page(page_no=i+1) usa o indice ABSOLUTO do documento inteiro (self._backend.page_count()), nao um indice relativo ao lote - logo lotes via page_range preservam numeracao nativa, diferente do approach de temp-PDF de 1 pagina da referencia (que sempre reporta page_no=1)."
  falsification_test: "Se eu converter um PDF sintetico/real de N paginas em 2 lotes via page_range=(1,k) e page_range=(k+1,N) e o page_no reportado no segundo lote NAO corresponder as paginas verdadeiras (ex.: comecar de 1 novamente), a hipotese de preservacao de page_no estaria errada e eu precisaria recalcular/offsetar page_no manualmente nos itens do lote."
  fix_rationale: "O fix ataca a causa raiz (pipeline mantendo o doc inteiro em memoria) reduzindo o escopo de cada chamada converter.convert() a um lote pequeno de paginas (ex. 15), liberando recursos (gc.collect()) entre lotes - exatamente o mecanismo que a referencia usa, mas via page_range nativo do docling em vez de PdfWriter manual, o que evita o problema de reset de page_no que o approach da referencia teria introduzido neste script (que depende de page_no real para ancoras)."
  blind_spots: "Nao testei ainda com um PDF real grande (apenas inspecao de codigo-fonte do docling); o comportamento de page_range pode variar entre backends (docling_parse vs outros) ou versoes futuras. Tambem nao verifiquei se ha overhead de reabrir o backend do PDF a cada chamada convert() em lote (acréscimo de I/O, mas aceitavel trade-off vs bad_alloc)."
- next_action: "Implementar convert_pdf_in_batches() (ou equivalente) em scripts/converte_livro.py usando converter.convert(pdf_path, page_range=(s,e)) em lotes de tamanho configuravel (ex. 15 paginas), com gc.collect() entre lotes, e um wrapper ChainedDoc leve que encadeia iterate_items() de cada lote; atualizar convert_pdf() para usar pypdf.PdfReader (import lazy) so para contar paginas totais e gerar os ranges. Depois adicionar testes deterministicos em tests/test_converte_livro.py cobrindo o chunking (via monkeypatch de uma converter.convert fake que retorna documentos sinteticos por lote) e rodar a suite completa."
- tdd_checkpoint: (vazio)

## Resolution

root_cause: "convert_pdf() em scripts/converte_livro.py faz uma unica chamada converter.convert(pdf_path) sobre o PDF inteiro, sem nenhum particionamento. Isso forca o pipeline docling (OCR + paginacao + geracao de imagens) a manter buffers de TODAS as paginas do livro na memoria simultaneamente, causando flood de std::bad_alloc em livros grandes. O fallback documentado de page_range em lotes nunca foi implementado (linhas 193-195 eram apenas um comentario)."
fix: "convert_pdf() reescrito para converter o PDF em LOTES de paginas via converter.convert(pdf_path, page_range=(s,e)) nativo do docling (sem PdfWriter/temp-PDF), com gc.collect() apos cada lote. Novo helper puro _page_batches(total_pages, batch_size) gera os ranges 1-indexados inclusivos (default batch_size=15, nunca 1). Novo helper _ChainedDoc encadeia iterate_items() dos DoclingDocument de cada lote sem precisar mesclar objetos internos do docling - reusa o mesmo contrato duck-typed (label.name/level/text/prov[0].page_no) que split_into_chapters/heading_histogram ja esperavam. main() ganhou --batch-size (default 15) e passa para convert_pdf. pypdf.PdfReader (ja dependencia declarada) e usado via import lazy so para contar paginas totais."
verification: "(1) Suite completa tests/test_converte_livro.py: 18 passed (9 testes novos cobrindo _page_batches, _ChainedDoc, split_into_chapters atraves de lotes encadeados, e convert_pdf com converter.convert/gc.collect mockados via monkeypatch - sem importar docling real). (2) Golden smoke (test_golden_smoke, marker slow) passou com docling REAL instalado em .venv-pdf contra tests/fixtures/sample.pdf. (3) Verificacao empirica adicional: convert_pdf(sample.pdf, cut_level=1, batch_size=1) rodado com .venv-pdf/Scripts/python.exe sobre o sample real (2 paginas) produziu page_no=[1, 2] nos itens - prova direta de que page_range preserva numeracao nativa de pagina mesmo no caso extremo de 1 pagina por lote, confirmando a hipotese do reasoning_checkpoint e refutando a alternativa eliminada (reset de page_no). (4) py_compile limpo em ambos os arquivos alterados. (5) VERIFICACAO HUMANA FINAL (2026-06-22T20:57): usuario rodou a versao corrigida sobre o PDF de livro grande REAL que originalmente estourava - pipeline processou multiplas paginas via RapidOCR por ~4 min e completou com 'OK' SEM nenhum std::bad_alloc. Os avisos de OCR vazio sao benignos (paginas so-imagem/em branco). VEREDITO: CONFIRMADO FIXED."
files_changed:
  - scripts/converte_livro.py
  - tests/test_converte_livro.py
