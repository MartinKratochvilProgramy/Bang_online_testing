from globals import *
from utils.window.switch_to_window import switch_to_window
from selenium.webdriver.common.by import By

def pick_characters():
    for username in USERS:
        switch_to_window(username)
        character_cards = driver.find_elements(By.XPATH, '//img[@alt="Character card"]')

        # pick first character
        character_cards[0].click()