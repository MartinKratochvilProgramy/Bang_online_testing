# Import the required libraries
import time
from tests.test_bang_mancato_barilo_vulcanic_CJ_WtK.main import test_bang_mancato_barilo_vulcanic_CJ_WtK
from tests.test_indiani_gatling_duel.main import test_indiani_gatling_duel_jourdonnais
from globals import *

# Navigate to the webpage
driver.get(ROUTE)

# test_bang_mancato_barilo_vulcanic_CJ_WtK()

test_bang_mancato_barilo_vulcanic_CJ_WtK()
test_indiani_gatling_duel_jourdonnais()
input()

# Close the web window
driver.quit()
