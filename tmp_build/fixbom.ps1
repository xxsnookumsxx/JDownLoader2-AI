$path = 'svn_trunk/src/jd/gui/swing/jdgui/views/settings/panels/anticaptcha/CaptchaWizardDialog.java'
$bytes = [System.IO.File]::ReadAllBytes($path)
if ($bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    $newBytes = ,0 * ($bytes.Length - 3)
    [Array]::Copy($bytes, 3, $newBytes, 0, $bytes.Length - 3)
    [System.IO.File]::WriteAllBytes($path, $newBytes)
    Write-Host "Removed BOM"
} else {
    Write-Host "No BOM"
}
