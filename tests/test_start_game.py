from utils.start_game.start_game import start_game
from utils.logging.log_passed import log_passed
from utils.logging.log_failed import log_failed
from utils.window.switch_to_window import switch_to_window
from utils.start_game.pick_characters import pick_characters
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from selenium.webdriver.common.by import By
from globals import *

def test_start_game():
    test_name = "Start game"
    try:
        start_game()

        for username in USERS:
            switch_to_window(username)

            character_cards = driver.find_elements(By.XPATH, '//img[@alt="Character card"]')
            if len(character_cards) != 2:
                raise Exception('Start game does not include 2 cards - ', username)
            
        pick_characters()

        if not switch_to_current_player_window():
            raise Exception('No player is on turn')
       
        log_passed(test_name)
    except Exception as e:
        log_failed(test_name, e)
