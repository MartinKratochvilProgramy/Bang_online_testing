from utils.login.login_all_users import login_all_users
from utils.logging.log_passed import log_passed
from utils.logging.log_failed import log_failed
from selenium.webdriver.common.by import By
from globals import *

def test_login():
    test_name = "Login all users"
    try:
        login_all_users()
        
        log_passed(test_name)
    except Exception as e:
        log_failed(test_name, e)
