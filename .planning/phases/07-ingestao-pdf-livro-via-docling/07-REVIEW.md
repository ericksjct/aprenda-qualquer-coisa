---
phase: 07-ingestao-pdf-livro-via-docling
reviewed: 2026-06-22T00:00:00Z
depth: standard
files_reviewed: 7
files_reviewed_list:
  - scripts/converte_livro.py
  - scripts/check-consistencia.sh
  - tests/conftest.py
  - tests/test_converte_livro.py
  - requirements-pdf.txt
  - .claude/skills/converte-livro/SKILL.md
  - .gitignore
findings:
  critical: 0
  warning: 2
  info: 3
  total: 5
status: issues_found
---

# Phase 07: Code Review Report

**Reviewed:** 2026-06-22
**Depth:** standard
**Files Reviewed:** 7
**Status:** issues_found

## Summary

Reviewed the opt-in docling book converter (`scripts/converte_livro.py`), its
test harness (`conftest.py`, `test_converte_livro.py`), the consistency-audit
shell script (`check-consistencia.sh`), and supporting docs/config.

The two security-relevant concerns called out (T-07-01 slug sanitization and
T-07-02 subprocess invocation) are both handled at the right layer:

- **Slug sanitization is solid.** `sanitize_slug` is allowlist-based
  (`^[a-z0-9-]+$`) with explicit `/`, `\`, `..` rejection, and is invoked in
  `main()` *before* any path construction or filesystem write (line 240,
  preceding `out_dir.mkdir` at 247). No path-traversal vector reaches a write.
- **markdownlint args are not shell-injectable by user text.** The argument
  vector is a fixed literal list plus a script-controlled `Path`; no user
  string is interpolated into a shell command line.
- **Env/memory guards are correctly ordered.** `OMP_NUM_THREADS` etc. are set
  at module top (lines 37-41) before any docling import, and docling imports
  are lazy (inside functions), so the guards are guaranteed live before the
  C++/OCR engine loads. `test_env_guards` pins this.

No critical issues. Two warnings concern the `shell=True` interaction on the
subprocess call; the rest are minor robustness/info items.

## Warnings

### WR-01: `shell=True` with a list argument neutralizes the FileNotFoundError skip and is brittle

**File:** `scripts/converte_livro.py:204-220`
**Issue:** `_run_markdownlint` calls `subprocess.run(["markdownlint", "--fix", str(write_path)], ..., shell=True)`. With `shell=True` Python does not search for or launch `markdownlint` directly — it launches the shell (`cmd.exe` on Windows / `/bin/sh` elsewhere) and hands it the command. Two consequences:

1. **The `except FileNotFoundError` graceful-skip never fires.** When the
   program is missing, `cmd.exe` itself launches successfully and returns a
   non-zero exit ("'markdownlint' is not recognized..."), so no
   `FileNotFoundError` is raised in Python. With `check=False` the failure is
   silently swallowed and the friendly install hint at lines 219-220 is dead
   code. The docstring's promise of a "skip gracioso" is not delivered on the
   missing-binary path.
2. **Platform-inconsistent list handling.** With `shell=True` and a list,
   POSIX `/bin/sh` uses only the first list element as the command and treats
   the rest as shell args to `sh` (so `--fix` and the path are effectively
   dropped), while Windows passes the joined string to `cmd.exe`. The same code
   thus behaves differently across OSes. The comment "necessario para execucao
   correta no Windows" addresses a Windows `.cmd`-shim PATH-resolution quirk,
   but the cross-platform list+shell combination is the wrong tool for it.

**Fix:** Prefer `shell=False` (the default) and resolve the launcher
explicitly, which restores the `FileNotFoundError` path and removes the shell
entirely:

```python
import shutil

def _run_markdownlint(write_path) -> None:
    exe = shutil.which("markdownlint") or shutil.which("markdownlint.cmd")
    if exe is None:
        print("    [!] Aviso: 'markdownlint' nao encontrado no sistema.")
        print("    Certifique-se de rodar: npm install -g markdownlint-cli")
        return
    subprocess.run(
        [exe, "--fix", str(write_path)],
        capture_output=True, text=True, check=False,
    )
```

If `shell=True` must be kept for the Windows shim, pass a single string
(`f'markdownlint --fix "{write_path}"'`) and detect the missing binary via the
shell's exit code instead of relying on `FileNotFoundError`. Note `write_path`
is script-controlled and slug-sanitized, so quoting is for correctness (spaces
in the temp/out path), not an injection fix.

### WR-02: Chapter filenames are not deduplicated — same slug overwrites silently

**File:** `scripts/converte_livro.py:139-148, 253-257`
**Issue:** `chapter_filename` derives the name from the chapter title, but the
filename is prefixed with the 1-based loop index (`{index:02d}-...`), so two
chapters with identical/empty titles still get distinct names
(`01-...`, `02-...`). That mostly protects against collisions. However, the
ASCII-stripping fallback collapses any title with no `[a-z0-9]` content (e.g. a
purely accented or symbolic heading) to the literal `"capitulo"` — combined
with the index prefix this is still unique, so there is no data-loss bug here.
The residual risk is only readability (`03-capitulo.md`, `07-capitulo.md`).
Flagged as a warning rather than info because empty/duplicate titles are a
realistic docling output for cover/section-break headings and the operator gets
no signal that titles were lost.

**Fix:** Optional — when the slug falls back to `"capitulo"`, log a notice so
the operator knows a heading produced no usable name, e.g.:

```python
if not slug:
    slug = "capitulo"
    print(f"    [!] capitulo {index}: titulo sem caracteres ASCII; usando '{slug}'")
```

No correctness change required; the index prefix already prevents overwrites.

## Info

### IN-01: `_page_of` assumes `prov[0].page_no` exists; partial-provenance items can raise

**File:** `scripts/converte_livro.py:67-72`
**Issue:** `_page_of` guards against an absent/empty `prov`, but if `prov` is a
non-empty list whose first element lacks `page_no`, `prov[0].page_no` raises
`AttributeError`. Real docling provenance objects always carry `page_no`, so
this is defensive-only, but it is the one spot in the pure helpers that reaches
into a nested attribute without `getattr`.

**Fix:** Mirror the `getattr` style used elsewhere:
```python
return getattr(prov[0], "page_no", None) if prov else None
```

### IN-02: `__doc__.splitlines()[0]` in `main` assumes the module docstring is present

**File:** `scripts/converte_livro.py:224`
**Issue:** `argparse.ArgumentParser(description=__doc__.splitlines()[0])` will
raise `AttributeError` if the module is ever run with docstrings stripped
(`python -OO`). Edge-case only; harmless under normal invocation.

**Fix:** `description=(__doc__ or "").splitlines()[0] if __doc__ else None` or
hardcode a short description string.

### IN-03: `check-consistencia.sh` `extra=...` pipeline can misreport on rg "no match"

**File:** `scripts/check-consistencia.sh:61-62`
**Issue:** `extra=$(... | rg -vc "^($NONCMD)$" ... || echo 0)`. `rg -c` exits
non-zero when there are zero matching lines, so the `|| echo 0` fallback fires
and assigns `0` — which is the intended value, so behavior is correct. The
subtlety: if the upstream `rg -oN` finds tokens but *all* are filtered out by
`rg -vc`, `rg -vc` prints `0` AND exits 1, so `echo 0` appends a second line,
making `extra` the two-line string `"0\n0"`. The subsequent
`[ "$extra" -eq 0 ]` would then error ("integer expression expected") under a
strict shell. In practice `sh` tolerates it and the test passes, but the
guard is fragile.

**Fix:** Drop the `-c` and count lines deterministically, e.g.:
```sh
extra=$(rg -oN '`/[a-z][a-z-]+`' "$f" 2>/dev/null | tr -d '`' | sed 's,^/,,' \
  | sort -u | rg -v "^($NONCMD)$" 2>/dev/null | wc -l | tr -d ' ')
```
`wc -l` always yields a single clean integer regardless of match count.

---

_Reviewed: 2026-06-22_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
