# Import the required libraries
import time
from tests.test_bang_mancato_barilo_vulcanic_CJ_WtK.main import test_bang_mancato_barilo_vulcanic_CJ_WtK
from globals import *
from utils.game.prepare_test import prepare_test

# Navigate to the webpage
driver.get(ROUTE)

test_bang_mancato_barilo_vulcanic_CJ_WtK()
prepare_test()

input()

# Close the web window
driver.quit()
