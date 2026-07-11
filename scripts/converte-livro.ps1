#requires -Version 5.1
<#
.SYNOPSIS
    Converte um livro-base em PDF para markdown por capitulo em .projetos/<slug>/livro/.

.DESCRIPTION
    Script-deliverable do passo "livro-base" do mentor. Idempotente e auto-suficiente:

      1. Cria os diretorios .projetos/<slug>/livro-fonte/ (onde voce poe o PDF) e
         .projetos/<slug>/livro/ (saida) automaticamente, se ainda nao existirem.
      2. Provisiona o venv opt-in .venv-pdf (Python 3.10+) e instala
         requirements-pdf.txt na PRIMEIRA execucao apenas.
      3. Descobre o PDF dentro de livro-fonte/ (ou use -Pdf <caminho>).
      4. Roda scripts/converte_livro.py em LOTES (page_range) para evitar std::bad_alloc.

    Roda LOCAL, NAO consome tokens. A 1a execucao baixa modelos (~2GB) e demora;
    o progresso e mostrado por lote.

.PARAMETER Slug
    Slug do projeto em kebab-case. Define a pasta .projetos/<Slug>/.

.PARAMETER Pdf
    Caminho do PDF do livro. Default: o primeiro *.pdf em .projetos/<Slug>/livro-fonte/.

.PARAMETER BatchSize
    Paginas convertidas por lote (default 15; so usado pelo motor docling).

.PARAMETER Engine
    auto (default) | vlm | docling. Em 'auto', usa o motor VLM (Unlimited-OCR,
    formulas em LaTeX + scan; requer GPU NVIDIA) quando nvidia-smi existe; senao
    docling (CPU, texto sem formula). O motor VLM tambem constroi o indice de
    consulta (livro/.index/) ao final.

.EXAMPLE
    # 1) cria as pastas, 2) voce poe o PDF em .projetos/minha-stack/livro-fonte/,
    # 3) rode de novo e ele converte:
    .\scripts\converte-livro.ps1 -Slug minha-stack

.EXAMPLE
    .\scripts\converte-livro.ps1 -Slug minha-stack -Pdf "C:\Downloads\livro.pdf" -BatchSize 8
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[a-z0-9-]+$')]
    [string]$Slug,

    [string]$Pdf,

    [ValidateRange(2, 100)]
    [int]$BatchSize = 15,

    [ValidateSet('auto', 'vlm', 'docling')]
    [string]$Engine = 'auto'
)

$ErrorActionPreference = 'Stop'

# Raiz do repo = pasta-pai de scripts/ (este arquivo vive em scripts/).
$RepoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $RepoRoot

$ProjDir = Join-Path $RepoRoot ".projetos\$Slug"
$SrcDir  = Join-Path $ProjDir  "livro-fonte"
$OutDir  = Join-Path $ProjDir  "livro"

# --- 1. Cria os diretorios automaticamente (idempotente) -------------------
New-Item -ItemType Directory -Force -Path $SrcDir | Out-Null
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

function Initialize-VenvOcr {
    $VenvDir = Join-Path $RepoRoot ".venv-ocr"
    $VenvPy  = Join-Path $VenvDir  "Scripts\python.exe"
    if (-not (Test-Path -LiteralPath $VenvPy)) {
        Write-Host "[*] Criando venv .venv-ocr (GPU) e instalando dependencias..." -ForegroundColor Cyan
        python -m venv $VenvDir
        & $VenvPy -m pip install --upgrade pip
        # duas etapas: torch CUDA de indice proprio; torchvision pinada com
        # --no-deps (o indice cu129 nao tem cp314 e o pip regride pra 0.1.6)
        & $VenvPy -m pip install torch==2.9.0 --index-url https://download.pytorch.org/whl/cu129
        & $VenvPy -m pip install --no-deps torchvision==0.24.0
        & $VenvPy -m pip install -r (Join-Path $RepoRoot "requirements-ocr.txt")
    }
    return $VenvPy
}

# --- 2. Descobre o PDF -----------------------------------------------------
if (-not $Pdf) {
    $found = Get-ChildItem -Path $SrcDir -Filter *.pdf -File -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if (-not $found) {
        # Sem PDF: se o aluno COLOU markdown em livro/, so constroi o indice.
        $mds = Get-ChildItem -Path $OutDir -Filter *.md -File -ErrorAction SilentlyContinue
        $hasGpu = [bool](Get-Command nvidia-smi -ErrorAction SilentlyContinue)
        if ($mds -and ($Engine -eq 'vlm' -or ($Engine -eq 'auto' -and $hasGpu))) {
            Write-Host "[*] livro/*.md ja presente; construindo apenas o indice de consulta..." -ForegroundColor Cyan
            $VenvPy = Initialize-VenvOcr
            & $VenvPy (Join-Path $RepoRoot "scripts\consulta_livro.py") --slug $Slug --build
            exit $LASTEXITCODE
        }
        if ($mds) {
            Write-Host "[i] livro/*.md presente, mas sem GPU NVIDIA nao ha indice de consulta:" -ForegroundColor Yellow
            Write-Host "    o tutor le os .md diretamente (sem busca semantica)." -ForegroundColor Yellow
            exit 0
        }
        Write-Host ""
        Write-Host "[i] Pastas prontas. Agora coloque o PDF do livro em:" -ForegroundColor Cyan
        Write-Host "      $SrcDir" -ForegroundColor Yellow
        Write-Host "    e rode este script de novo (ou passe -Pdf <caminho>)." -ForegroundColor Cyan
        Write-Host "    (Livro em .md? Cole os arquivos em $OutDir e rode de novo.)" -ForegroundColor Cyan
        Write-Host ""
        exit 0
    }
    $Pdf = $found.FullName
}
if (-not (Test-Path -LiteralPath $Pdf)) {
    throw "PDF nao encontrado: $Pdf"
}

# --- 3. Escolhe o motor -----------------------------------------------------
if ($Engine -eq 'auto') {
    $Engine = if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) { 'vlm' } else { 'docling' }
    Write-Host "[*] Motor escolhido automaticamente: $Engine" -ForegroundColor Cyan
}

# --- 4. Provisiona o venv do motor (idempotente) ----------------------------
if ($Engine -eq 'vlm') {
    $VenvPy = Initialize-VenvOcr
} else {
    $VenvDir = Join-Path $RepoRoot ".venv-pdf"
    $VenvPy  = Join-Path $VenvDir  "Scripts\python.exe"
    if (-not (Test-Path -LiteralPath $VenvPy)) {
        Write-Host "[*] Criando venv .venv-pdf (Python 3.10+) e instalando dependencias..." -ForegroundColor Cyan
        python -m venv $VenvDir
        & $VenvPy -m pip install --upgrade pip
        & $VenvPy -m pip install -r (Join-Path $RepoRoot "requirements-pdf.txt")
    }
}

# --- 5. Pre-aviso obrigatorio ---------------------------------------------
Write-Host ""
Write-Host "[*] Convertendo o livro (roda LOCAL, NAO consome tokens)." -ForegroundColor Cyan
Write-Host "    Vai demorar e mostra o progresso. A 1a execucao baixa modelos (varios GB)." -ForegroundColor Cyan
Write-Host "    PDF:   $Pdf"
Write-Host "    Saida: $OutDir"
Write-Host ""

# --- 6. Converte ------------------------------------------------------------
if ($Engine -eq 'vlm') {
    # VLM: formulas em LaTeX + imagens de pagina; ~50s/pagina em GPU 12GB
    & $VenvPy (Join-Path $RepoRoot "scripts\converte_livro_vlm.py") $Pdf --slug $Slug
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    # constroi o indice de consulta (livro/.index/) sobre o markdown gerado
    & $VenvPy (Join-Path $RepoRoot "scripts\consulta_livro.py") --slug $Slug --build
} else {
    & $VenvPy (Join-Path $RepoRoot "scripts\converte_livro.py") `
        $Pdf --slug $Slug --batch-size $BatchSize
}
exit $LASTEXITCODE
