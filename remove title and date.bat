@ECHO OFF
FOR /F "delims=*" %%A IN ('dir /b *.MKV') DO "C:/Program Files/MKVToolNix\mkvpropedit.exe" -d title -d date "%%A"
(goto) 2>nul & del "%~f0"