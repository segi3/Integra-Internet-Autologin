#o::
run cmd.exe
WinWait, ahk_exe cmd.exe
WinWaitActive, ahk_exe cmd.exe
Send D:{Enter}
Send cd D:\file\path{Enter}
Send python login-akses-internet-integra.py{Enter}
Sleep, 11000
Send exit{Enter}
return