# Import the required libraries

from selenium.webdriver.common.by import By
from utils.login.login_all_users import login_all_users
from utils.window.switch_to_window import switch_to_window
import time
from globals import *

# Navigate to the webpage
driver.get(ROUTE)

login_all_users()

switch_to_window("a")

time.sleep(10)

# Close the web window
driver.quit()
