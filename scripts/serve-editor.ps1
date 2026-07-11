# Sobe o editor do navegador (ide.html) em http://127.0.0.1:<porta>.
#
# O servidor serve o ide.html E expoe uma mini-API de arquivos rooteada em
# .projetos/ (a casa dos projetos do aluno): a pagina abre ja com a arvore de
# todos os projetos carregada, sem dialogo de "abrir pasta" — e por isso
# funciona em QUALQUER navegador. So PowerShell nativo do Windows
# (HttpListener): sem Python, sem Node, sem instalacao.
#
# API (leitura/escrita restritas a .projetos/):
#   GET /api/tree              -> arvore JSON de .projetos/
#   GET /api/file?path=<rel>   -> conteudo do arquivo
#   PUT /api/file?path=<rel>   -> salva o corpo da requisicao no arquivo
#
# Entrada normal: dois cliques em abrir-editor.cmd (na raiz do repo).
# Compativel com Windows PowerShell 5.1 (o que o .cmd invoca).

$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot
$ProjDir  = Join-Path $RepoRoot ".projetos"
New-Item -ItemType Directory -Force -Path $ProjDir | Out-Null

$SKIP = @('.git', 'node_modules', '__pycache__', '.pytest_cache',
          '.venv-pdf', '.venv-ocr', '.index', '.paginas')

$types = @{
    '.html' = 'text/html; charset=utf-8'
    '.js'   = 'text/javascript; charset=utf-8'
    '.css'  = 'text/css; charset=utf-8'
    '.json' = 'application/json; charset=utf-8'
    '.md'   = 'text/plain; charset=utf-8'
    '.png'  = 'image/png'
    '.jpg'  = 'image/jpeg'
    '.svg'  = 'image/svg+xml'
    '.ico'  = 'image/x-icon'
}

function Get-Tree($dir) {
    $items = @()
    $entries = Get-ChildItem -LiteralPath $dir -Force |
        Sort-Object @{ e = { -not $_.PSIsContainer } }, Name
    foreach ($e in $entries) {
        if ($SKIP -contains $e.Name) { continue }
        if ($e.PSIsContainer) {
            $items += @{ name = $e.Name; type = 'dir'; children = @(Get-Tree $e.FullName) }
        } else {
            $items += @{ name = $e.Name; type = 'file' }
        }
    }
    # sem o operador virgula: o pipeline desenrola os itens e o @() de quem
    # chama re-coleta em array — com a virgula o JSON sai duplamente aninhado
    return $items
}

function Resolve-ProjPath($rel) {
    # path-safety: tudo da API vive DENTRO de .projetos/
    if (-not $rel) { return $null }
    $full = [IO.Path]::GetFullPath((Join-Path $ProjDir $rel))
    $prefix = $ProjDir + [IO.Path]::DirectorySeparatorChar
    if ($full.StartsWith($prefix)) { return $full }
    return $null
}

# porta livre a partir da 8123
$listener = $null
$port = 8123
while (-not $listener) {
    try {
        $listener = New-Object System.Net.HttpListener
        $listener.Prefixes.Add("http://127.0.0.1:$port/")
        $listener.Start()
    } catch {
        $listener = $null
        $port++
        if ($port -gt 8143) { throw "nenhuma porta livre entre 8123-8143" }
    }
}

$url = "http://127.0.0.1:$port/ide.html"
Write-Host ""
Write-Host "[*] Editor no ar: $url" -ForegroundColor Cyan
Write-Host "    DEIXE esta janela aberta enquanto edita." -ForegroundColor Yellow
Write-Host "    Feche-a (ou Ctrl+C) quando terminar." -ForegroundColor Yellow
Write-Host ""

try { Start-Process "msedge" $url } catch { Start-Process $url }

while ($listener.IsListening) {
    $ctx = $listener.GetContext()
    $req = $ctx.Request
    $res = $ctx.Response
    try {
        $path = $req.Url.AbsolutePath
        if ($path -eq '/api/tree') {
            $json = ConvertTo-Json @(Get-Tree $ProjDir) -Depth 64 -Compress
            $bytes = [Text.Encoding]::UTF8.GetBytes($json)
            $res.ContentType = 'application/json; charset=utf-8'
            $res.ContentLength64 = $bytes.Length
            $res.OutputStream.Write($bytes, 0, $bytes.Length)
        }
        elseif ($path -eq '/api/file') {
            $full = Resolve-ProjPath ([Uri]::UnescapeDataString($req.QueryString['path']))
            if (-not $full) { $res.StatusCode = 403 }
            elseif ($req.HttpMethod -eq 'GET') {
                if (Test-Path -LiteralPath $full -PathType Leaf) {
                    $bytes = [IO.File]::ReadAllBytes($full)
                    $res.ContentType = 'text/plain; charset=utf-8'
                    $res.ContentLength64 = $bytes.Length
                    $res.OutputStream.Write($bytes, 0, $bytes.Length)
                } else { $res.StatusCode = 404 }
            }
            elseif ($req.HttpMethod -eq 'PUT') {
                $fs = [IO.File]::Create($full)
                $req.InputStream.CopyTo($fs)
                $fs.Close()
                $res.StatusCode = 204
            }
            else { $res.StatusCode = 405 }
        }
        else {
            # estatico (o proprio ide.html), rooteado no repo
            $rel = [Uri]::UnescapeDataString($path).TrimStart('/')
            if (-not $rel) { $rel = 'ide.html' }
            $full = [IO.Path]::GetFullPath((Join-Path $RepoRoot $rel))
            if ($full.StartsWith($RepoRoot) -and (Test-Path -LiteralPath $full -PathType Leaf)) {
                $bytes = [IO.File]::ReadAllBytes($full)
                $ext = [IO.Path]::GetExtension($full).ToLower()
                if ($types[$ext]) { $res.ContentType = $types[$ext] }
                else { $res.ContentType = 'application/octet-stream' }
                $res.ContentLength64 = $bytes.Length
                $res.OutputStream.Write($bytes, 0, $bytes.Length)
            } else {
                $res.StatusCode = 404
            }
        }
    } catch {
        try { $res.StatusCode = 500 } catch {}
    } finally {
        $res.Close()
    }
}
