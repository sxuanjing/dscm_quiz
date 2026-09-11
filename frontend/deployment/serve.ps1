param(
  [int]$Port = 4173
)

Set-Location $PSScriptRoot\..\
& npx.cmd serve dist --listen $Port
