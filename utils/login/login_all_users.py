from selenium.webdriver.common.by import By
from utils.login.login_user import login_user
from utils.window.open_new_window import open_new_window
from utils.window.switch_to_window import switch_to_window
from globals import *

def login_all_users():
    for i, username in enumerate(USERS):
        if i > 0:
            open_new_window(ROUTE)
        login_user(username)
        
        username_field = driver.find_elements(By.XPATH, f"//*[contains(text(),'{username}')]")
        if len(username_field) == 0:
            raise Exception('Username missing after login.')

    switch_to_window(USERS[0])