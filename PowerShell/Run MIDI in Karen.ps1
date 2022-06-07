#Mostly made because I didn't want to have to type in all the stuff manually.
#You'll need to place your MIDIs in the same directory too as KAREN.EXE / KAREN.COM. I didn't feel like (plus new to PowerShell) finding a way to make it to where it'll look in a subfolder.
#This program also assumes you have your DOSBox installed in the default location (change it on the Start-Process line if in other location) 
#Program also assumes that you have set up a config in DOSBox's configuration file to automatically mount and direct DOSBox to your KAREN Folder upon booting up the program.
#You will need DosJP for KAREN to even work in DOSBox to begin with. You can get it here: https://www.mediafire.com/file/ys1sokwcdciowd7/dosjp.zip/file

[void][Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic')
Add-Type -AssemblyName PresentationFramework

#Input Box 1
$title = 'KAREN MIDI Input'
$msg   = 'Enter the name of your MIDI file (case sensitive)'

$text = [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)

$midifile = $text

#Input Box 2
$title = 'Type of MIDI'
$msg   = 'Enter  One of these types of MIDI: MS (General Midi) / MX (Yamaha XG) / M8 (SC88) / MP (Pro) / MM (General Midi)'

$typetext = [Microsoft.VisualBasic.Interaction]::InputBox($msg, $title)

$miditype = $typetext

#Open the Program
Start-Process -FilePath "C:\Program Files (x86)\DOSBox-0.74-3\DOSBox.exe"
$DBProcess = (Get-Process DOSBox).Id
$wshell = New-Object -ComObject wscript.shell
#$wshell.AppActivate($DBProcess)

#Sleep to give time to load
Start-Sleep -Seconds 1.35

#If Statements to type in the correct prompt based on input
if ( $miditype -eq "MS")
{

$wshell.SendKeys("karen /ms /i6")
Start-Sleep -milliseconds 3
$wshell.SendKeys(" ")
Start-Sleep -milliseconds 5
$wshell.SendKeys("$midifile")

Start-Sleep -milliseconds 1000

$wshell.SendKeys('~')
}

elseif ($miditype -eq "MX")
{

$wshell.SendKeys("karen /mx /i6")
Start-Sleep -milliseconds 3
$wshell.SendKeys(" ")
Start-Sleep -milliseconds 5
$wshell.SendKeys("$midifile")
}

elseif ($miditype -eq "M8")
{

$wshell.SendKeys("karen /m8 /i6")
Start-Sleep -milliseconds 3
$wshell.SendKeys(" ")
Start-Sleep -milliseconds 5
$wshell.SendKeys("$midifile")
}

elseif ($miditype -eq "MP")
{

$wshell.SendKeys("karen /mp /i6")
Start-Sleep -milliseconds 3
$wshell.SendKeys(" ")
Start-Sleep -milliseconds 5
$wshell.SendKeys("$midifile")
}

elseif ($miditype -eq "MM")
{

$wshell.SendKeys("karen /mm /i6")
Start-Sleep -milliseconds 3
$wshell.SendKeys(" ")
Start-Sleep -milliseconds 5
$wshell.SendKeys("$midifile")
}

#Anything that isn't one of the names above will end the program and close DOSBox
else {
[System.Windows.MessageBox]::Show('Not a correct file name. Please try again.' ,'Not a correct file type.')
Stop-Process -Name DOSBox
exit
}

#Sleep to give time for the file to type in all the inputs
Start-Sleep -milliseconds 1000

#Hits enter for you
$wshell.SendKeys('~')

#Mild sleep before message box
Start-Sleep -Milliseconds 500

#Message Box showing some of the hotkeys since there is no official documentation I can find. This is not a complete set of the hotkeys and I sadly do not know Japanese so I can't find them all. 
#This was mostly trial and error.
$Msg = @'
F1 - F10 will change the color :)
Q quits the application
Shift will speed up the song
M changes playback
C enables chord view
'@
[System.Windows.MessageBox]::Show($Msg,'Some Hotkeys for You','OK','Information')