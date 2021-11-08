@ECHO OFF
FOR /F "delims=*" %%A IN ('dir /b *.MKV') DO (
"C:\Program Files\MKVToolNix\mkvmerge.exe" -o ".\edit\%%A" --default-track "1:1" --default-track 2:1 "%%A"
move /Y "edit\%%A" "%cd%"
)
rmdir "edit"
(goto) 2>nul & del "%~f0"