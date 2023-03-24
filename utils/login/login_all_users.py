from utils.login.login_user import login_user
from utils.window.open_new_window import open_new_window
from globals import *

def login_all_users():
    for i, username in enumerate(USERS):
        if i > 0:
            open_new_window(ROUTE)
        login_user(username)