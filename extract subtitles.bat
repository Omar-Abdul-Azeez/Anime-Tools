@ECHO OFF
FOR /F "delims=*" %%A IN ('dir /b *.MKV') DO "C:/Program Files/MKVToolNix\mkvextract.exe" "%%A" tracks 2:"./edit/%%~nA.mks"
(goto) 2>nul & del "%~f0"