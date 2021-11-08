@ECHO OFF
FOR /F "delims=*" %%A IN ('dir /b *.MKV') DO (
"C:\Program Files\MKVToolNix\mkvmerge.exe" -o "./edit/%%A" "%%A" "%%~nA.mks"
move /Y "edit\%%A" "%cd%"
del "%%~nA.mks"
)
rmdir "edit"
(goto) 2>nul & del "%~f0"