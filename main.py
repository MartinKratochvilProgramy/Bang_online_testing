# Import the required libraries
import time
from tests.test_bang.test_bang import test_bang
from globals import *

# Navigate to the webpage
driver.get(ROUTE)

test_bang()

input()

# Close the web window
driver.quit()
