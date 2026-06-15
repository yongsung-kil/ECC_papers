<#
LDPC 논문 수집 작업을 Windows 작업 스케줄러에 등록한다.

사용법(PowerShell, 일반 권한이면 현재 사용자 작업으로 등록됨):
    powershell -ExecutionPolicy Bypass -File scripts\register_task.ps1
    powershell -ExecutionPolicy Bypass -File scripts\register_task.ps1 -IntervalHours 3

해제:
    schtasks /Delete /TN "LDPC_Paper_Collector" /F
#>
param(
    [int]$IntervalHours = 6,          # 몇 시간마다 실행할지
    [string]$StartTime  = "09:00",    # 첫 실행 시각
    [string]$TaskName   = "LDPC_Paper_Collector"
)

$ErrorActionPreference = "Stop"
$bat = Join-Path $PSScriptRoot "run_collect.bat"

if (-not (Test-Path $bat)) {
    throw "run_collect.bat 를 찾을 수 없습니다: $bat"
}

# 6시간마다(=하루 4회) 반복 실행. 경로에 공백/한글이 있어도 따옴표로 안전 처리.
schtasks /Create `
    /TN $TaskName `
    /TR "`"$bat`"" `
    /SC HOURLY `
    /MO $IntervalHours `
    /ST $StartTime `
    /F

Write-Host ""
Write-Host "[OK] '$TaskName' 등록 완료 — $IntervalHours 시간마다 실행 (첫 실행 $StartTime)" -ForegroundColor Green
Write-Host "지금 바로 한 번 실행해 테스트: schtasks /Run /TN `"$TaskName`""
Write-Host "등록 해제:                  schtasks /Delete /TN `"$TaskName`" /F"
