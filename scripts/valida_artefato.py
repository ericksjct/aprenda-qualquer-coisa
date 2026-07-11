"""Valida artefatos do mentor mecanicamente (stdlib, sem dependencias).

Uso:
  python scripts/valida_artefato.py <arquivo-ou-pasta> [...]
  python scripts/valida_artefato.py --self-test

- Arquivo .md   -> subset markdownlint: MD009, MD012, MD025, MD040, MD047.
- Outro arquivo -> campos obrigatorios do scaffold (reference.md, "Formato do scaffold").
- Pasta         -> varre .md sempre; outros arquivos so se parecem scaffold (contem
  TODO(human) ou MARCO), pra nao acusar asset que nunca foi scaffold.

Sai com codigo 1 se houver erro; imprime arquivo:linha: regra mensagem.
"""

import re
import sys
from pathlib import Path

SCAFFOLD_FIELDS = (
    "META:", "PORQUE:", "PRESSUPOE:", "ARQUIVOS:", "EXEMPLO-DE-RESULTADO:",
    "PERGUNTA-GUIA:", "DONE:", "TODO(human)", "PISTA",
)

FENCE_RE = re.compile(r"^\s*(```+|~~~+)\s*(\S*)")


def check_md(text):
    errors = []
    lines = text.split("\n")
    h1_count = 0
    in_fence = False
    prev_blank = False
    for i, line in enumerate(lines, 1):
        fence = FENCE_RE.match(line)
        if fence:
            if not in_fence and not fence.group(2):
                errors.append((i, "MD040", "bloco de codigo sem linguagem"))
            in_fence = not in_fence
            prev_blank = False
            continue
        if in_fence:
            continue
        if line != line.rstrip():
            errors.append((i, "MD009", "espaco no fim da linha"))
        if re.match(r"^# \S", line):
            h1_count += 1
            if h1_count > 1:
                errors.append((i, "MD025", "mais de um cabecalho nivel 1"))
        blank = not line.strip()
        if blank and prev_blank:
            errors.append((i, "MD012", "mais de uma linha em branco consecutiva"))
        prev_blank = blank
    if text and (not text.endswith("\n") or text.endswith("\n\n")):
        errors.append((len(lines), "MD047",
                       "arquivo deve terminar com exatamente 1 quebra de linha"))
    return errors


def check_scaffold(text):
    return [(1, "SCAFFOLD", "campo obrigatorio ausente: " + f)
            for f in SCAFFOLD_FIELDS if f not in text]


def looks_like_scaffold(text):
    return "TODO(human)" in text or "MARCO" in text


def iter_targets(paths):
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for f in sorted(path.rglob("*")):
                if not f.is_file() or ".git" in f.parts:
                    continue
                if f.suffix == ".md":
                    yield f, "md"
                else:
                    try:
                        text = f.read_text(encoding="utf-8")
                    except (UnicodeDecodeError, OSError):
                        continue
                    if looks_like_scaffold(text):
                        yield f, "scaffold"
        elif path.is_file():
            yield path, "md" if path.suffix == ".md" else "scaffold"
        else:
            print(f"aviso: {p} nao existe", file=sys.stderr)


def self_test():
    ok_md = "# Titulo\n\nTexto.\n\n```python\nx = 1\n```\n"
    assert check_md(ok_md) == []
    bad_md = "# A\n\n\n# B\ncodigo:  \n```\nx\n```"
    rules = {r for _, r, _ in check_md(bad_md)}
    assert {"MD009", "MD012", "MD025", "MD040", "MD047"} <= rules
    ok_sc = ("/*\n  MARCO 01 -- x\n  META: a\n  PORQUE: b\n  PRESSUPOE: c\n"
             "  ARQUIVOS: d\n  EXEMPLO-DE-RESULTADO: e\n  PERGUNTA-GUIA: f\n"
             "  DONE: g\n*/\n// TODO(human): h\n// PISTA: i\n")
    assert check_scaffold(ok_sc) == []
    assert any("META:" in m for _, _, m in check_scaffold("// TODO(human)"))


def main(argv):
    if argv == ["--self-test"]:
        self_test()
        print("self-test ok")
        return 0
    if not argv:
        print(__doc__)
        return 2
    total = 0
    for path, kind in iter_targets(argv):
        text = path.read_text(encoding="utf-8")
        errors = check_md(text) if kind == "md" else check_scaffold(text)
        for line, rule, msg in errors:
            print(f"{path}:{line}: {rule} {msg}")
        total += len(errors)
    if total:
        print(f"\n{total} erro(s).")
        return 1
    print("ok: nenhum erro.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
