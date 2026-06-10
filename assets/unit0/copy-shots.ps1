# shots -> assets/unit0/ 복사 스크립트 (와일드카드 방식, 한글 인코딩 문제 없음)
$shots = "C:\work\edu_data\PBL\tools\capture-watcher\_capture\shots"
$dest  = "C:\work\edu_data\PBL\cs_intermediate_lab\assets\unit0"

1..8 | ForEach-Object {
    $n    = $_.ToString("D2")
    $file = Get-ChildItem $shots -Filter "*u0-s$n*" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($file) {
        $newName = "u0-s$n.png"
        Copy-Item $file.FullName (Join-Path $dest $newName) -Force
        Write-Host "OK  u0-s$n : $($file.Name)"
    } else {
        Write-Host "MISSING: u0-s$n"
    }
}
Write-Host "Done."
