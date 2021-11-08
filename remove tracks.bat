@ECHO OFF
FOR /F "delims=*" %%A IN ('dir /b *.MKV') DO "C:\Program Files\MKVToolNix\mkvmerge.exe" -o "./edit/%%A" -a !2 -s !4 "%%A"
PAUSE
move /Y "edit\*.*" "%cd%"
rmdir "edit"
(goto) 2>nul & del "%~f0"