#Requires -RunAsAdministrator
#Made when I was working as a Tech to help with Printer Issues

Write-Output "Stopping the Spooler"
write-host "`n"
Sleep -Seconds 2
Stop-Service Spooler -PassThru
write-host "`n"
Invoke-Item C:\Windows\System32\spool\PRINTERS
$Input = Read-Host -Prompt "Press any key start up the services again. Do this AFTER you cleared out the queue"
Write-Output "Starting the Services.."
write-host "`n"
Sleep -Seconds 2
Start-Service Spooler -PassThru
write-host "`n"
[System.Windows.MessageBox]::Show('All Done!')
exit