set TEST_BANG=t_bang_dnpauey
set TEST_INDIANI=t_indiani_dnpauey
set TEST_PANICO=t_panico_dnpauey
set TEST_PRIGIONE=t_prigione_dnpauey
start node "C:\Users\martv\Desktop\scratch\Bang_online\server\build\server.js"

python -B "c:\Users\martv\Desktop\scratch\Bang_online_testing\main.py"

taskkill /FI "WINDOWTITLE eq C:\Program Files\nodejs\node.exe*" /F