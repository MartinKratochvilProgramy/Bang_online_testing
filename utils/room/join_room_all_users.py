from utils.room.create_room import create_room
from utils.window.switch_to_window import switch_to_window
from utils.room.join_room import join_room
from globals import *

def join_room_all_users():
    for i, username in enumerate(USERS):
        if i == 0:
            # first user creates room
            create_room(username)
        else:
            switch_to_window(username)
            join_room()

    driver.switch_to.window(driver.window_handles[0])  

    # switch_to_window(USERS[0])