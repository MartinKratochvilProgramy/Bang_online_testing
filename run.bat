set TEST_PLAYER=fgbwrighoqfqwehfnwog
start node "C:\Users\martv\Desktop\scratch\Bang_online\server\build\server.js"

python -B "c:\Users\martv\Desktop\scratch\Bang_online_testing\main.py"

taskkill /FI "WINDOWTITLE eq C:\Program Files\nodejs\node.exe*" /F