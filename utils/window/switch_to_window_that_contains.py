from globals import *
from utils.window.switch_to_window import switch_to_window
from selenium.webdriver.common.by import By

def switch_to_window_that_contains_text(text: str):
    for username in USERS:
        switch_to_window(username)
        
        elements = driver.find_elements(By.XPATH, f"//*[contains(text(),'{text}')]")
        if len(elements) > 0:
            return True
        
    return False