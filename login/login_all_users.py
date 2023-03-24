from login.login_user import login_user
from open_new_window import open_new_window

def login_all_users(users, route, driver):
    for i, username in enumerate(users):
        if i > 0:
            open_new_window(route, driver)
        login_user(username, driver)