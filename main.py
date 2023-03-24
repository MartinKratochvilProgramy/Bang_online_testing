# Import the required libraries
import time

from selenium.webdriver.common.by import By
from utils.login.login_all_users import login_all_users
from utils.window.switch_to_window import switch_to_window
from utils.room.join_room_all_users import join_room_all_users
from globals import *

# Navigate to the webpage
driver.get(ROUTE)

login_all_users()

join_room_all_users()

time.sleep(1)

# Close the web window
driver.quit()
