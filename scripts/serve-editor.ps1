# Sobe o editor do navegador (ide.html) em http://127.0.0.1:<porta>.
#
# Por que um servidor: a File System Access API (abrir/salvar pasta) so existe
# em contexto seguro (https ou localhost) — dois cliques no ide.html (file://)
# NAO funcionam em navegador nenhum. Este script usa so o PowerShell nativo do
# Windows (HttpListener): sem Python, sem Node, sem instalacao.
#
# Entrada normal: dois cliques em abrir-editor.cmd (na raiz do repo).

$ErrorActionPreference = 'Stop'
$RepoRoot = Split-Path -Parent $PSScriptRoot

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

# Edge existe em todo Windows; se falhar, navegador padrao
try { Start-Process "msedge" $url } catch { Start-Process $url }

while ($listener.IsListening) {
    $ctx = $listener.GetContext()
    $res = $ctx.Response
    try {
        $rel = [Uri]::UnescapeDataString($ctx.Request.Url.AbsolutePath).TrimStart('/')
        if (-not $rel) { $rel = 'ide.html' }
        $full = [IO.Path]::GetFullPath((Join-Path $RepoRoot $rel))
        if ($full.StartsWith($RepoRoot) -and (Test-Path -LiteralPath $full -PathType Leaf)) {
            $bytes = [IO.File]::ReadAllBytes($full)
            $ext = [IO.Path]::GetExtension($full).ToLower()
            $res.ContentType = if ($types[$ext]) { $types[$ext] } else { 'application/octet-stream' }
            $res.ContentLength64 = $bytes.Length
            $res.OutputStream.Write($bytes, 0, $bytes.Length)
        } else {
            $res.StatusCode = 404
        }
    } catch {
        $res.StatusCode = 500
    } finally {
        $res.Close()
    }
}
