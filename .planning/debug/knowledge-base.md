# GSD Debug Knowledge Base

Resolved debug sessions. Used by `gsd-debugger` to surface known-pattern hypotheses at the start of new investigations.

---

## bad-alloc-converte-livro — Flood de std::bad_alloc ao converter livros grandes via docling
- **Date:** 2026-06-22
- **Error patterns:** std::bad_alloc, converte_livro.py, docling, converter.convert, OCR, memoria, page_range, livro grande, RapidOCR
- **Root cause:** convert_pdf() fazia uma unica converter.convert(pdf_path) sobre o PDF inteiro, forcando o pipeline docling/OCR a manter buffers de todas as paginas em memoria simultaneamente, estourando alocacao (std::bad_alloc) em livros grandes. O fallback de page_range em lotes estava apenas documentado em comentario, nunca implementado.
- **Fix:** Reescrita de convert_pdf() para converter em lotes via converter.convert(pdf_path, page_range=(s,e)) nativo do docling, com gc.collect() entre lotes. page_range preserva o page_no verdadeiro (indice absoluto), preservando as ancoras <!-- page: N -->. Novos helpers _page_batches() e _ChainedDoc; flag --batch-size (default 15); pypdf.PdfReader (import lazy) so para contar paginas totais.
- **Files changed:** scripts/converte_livro.py, tests/test_converte_livro.py
---
