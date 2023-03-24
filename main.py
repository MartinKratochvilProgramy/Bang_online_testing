# Import the required libraries
import time
from tests.test_login import test_login
from tests.test_join_room import test_join_room
from tests.test_start_game import test_start_game
from tests.test_bang import test_bang
from globals import *

# Navigate to the webpage
driver.get(ROUTE)

# login_all_users()

# join_room_all_users()

# start_game()

# pick_characters()

test_login()
test_join_room()
test_start_game()
test_bang()

input()

# Close the web window
driver.quit()
