@ECHO OFF
FOR /F "delims=*" %%A IN ('dir /b *.mp4') DO (
"C:\Program Files\MKVToolNix\mkvmerge.exe" -o "./edit/%%~nA.mkv" "%%A"
rm "%%A"
move /Y "edit\%%~nA.mkv" "%cd%"
)
rmdir "edit"
(goto) 2>nul & del "%~f0"