$word = New-Object -ComObject Word.Application
$word.Visible = $false

$workspace = Get-Location
$files = @(
    "SanchezYrure_Adrian_22292401_portfolio2.docx",
    "A4_SanchezYrure_Adrian.docx"
)

foreach ($f in $files) {
    $docxPath = Join-Path $workspace $f
    $pdfPath = [System.IO.Path]::ChangeExtension($docxPath, ".pdf")
    Write-Host "Converting $f to PDF..."
    $doc = $word.Documents.Open($docxPath)
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $doc.Close()
    Write-Host "Created: $pdfPath"
}

$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
Write-Host "PDF conversion finished successfully."
