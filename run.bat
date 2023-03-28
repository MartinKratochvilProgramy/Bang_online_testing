set TEST_BANG=t_bang_dnpauey
set TEST_INDIANI=t_indiani_dnpauey
set TEST_PANICO=t_panico_dnpauey
set TEST_PRIGIONE=t_prigione_dnpauey
set TEST_EMPORIO=t_emporio_dnpauey
set TEST_STK=t_StK_dnpauey
set BART_CASSIDY=t_bart_dnpauey
set BJ_ElG=t_BJ_ElG_dnpauey
@REM start node "C:\Users\martv\Desktop\scratch\Bang_online\server\build\server.js"
start node "C:\Users\martin.kratochvil\Desktop\scratch\Bang_online\server\build\server.js"

@REM python -B "c:\Users\martv\Desktop\scratch\Bang_online\Bang_online_testing\main.py"
python -B "c:\Users\martin.kratochvil\Desktop\scratch\Bang_online\Bang_online_testing\main.py"

taskkill /FI "WINDOWTITLE eq C:\Program Files\nodejs\node.exe*" /F