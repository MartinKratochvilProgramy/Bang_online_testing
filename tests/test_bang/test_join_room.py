from utils.room.join_room_all_users import join_room_all_users
from utils.logging.log_passed import log_passed
from utils.logging.log_failed import log_failed
from utils.window.switch_to_window import switch_to_window
from utils.locators.page_contains import page_contains_by_text
from utils.window.switch_to_window_that_contains import switch_to_window_that_contains_text
from selenium.webdriver.common.by import By
from globals import *

def test_join_room():
    test_name = "Join room all users"
    try:
        join_room_all_users()
        for username in USERS:
            switch_to_window(username)
            if not page_contains_by_text(username):
                raise Exception('Username not found in room')
            
        if not switch_to_window_that_contains_text('START GAME'):
            raise Exception('Unable to start game')

        
        log_passed(test_name)
    except Exception as e:
        log_failed(test_name, e)
