set TEST_BANG=t_bang_dnpaueyIPoe
set TEST_INDIANI=t_indiani_dnpaueyIPoe
start node "C:\Users\martv\Desktop\scratch\Bang_online\server\build\server.js"

python -B "c:\Users\martv\Desktop\scratch\Bang_online_testing\main.py"

taskkill /FI "WINDOWTITLE eq C:\Program Files\nodejs\node.exe*" /F