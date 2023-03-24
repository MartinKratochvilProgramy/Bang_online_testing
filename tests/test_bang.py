from selenium.webdriver.common.by import By
from utils.logging.log_passed import log_passed
from utils.logging.log_failed import log_failed
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from utils.window.switch_to_window import switch_to_window
from utils.game.use_blue_card import use_blue_card
from utils.game.use_bang import use_bang
from utils.game.use_mancato import use_mancato
from utils.locators.page_contains import page_contains_by_text
from globals import *

def test_bang():
    test_name = "Test Bang!"
    try:
        switch_to_current_player_window()
        
        use_blue_card('Barilo')

        target = USERS[1]
        # USE BANG! #1
        use_bang(target)
        switch_to_window(target)
        if not page_contains_by_text('Lose health'):
            raise Exception('Target not losing health after Bang!')
        use_mancato()
        
        switch_to_current_player_window()
        if not page_contains_by_text('End turn'):
            raise Exception('No End turn after Mancato reaction from target')
        
        # USE VULCANIC, RESET BANG!
        use_blue_card('Vulcanic')

        # USE BANG! #2
        use_bang(target)
        switch_to_window(target)
        if not page_contains_by_text('Lose health'):
            raise Exception('Target not losing health after Bang!')
        use_mancato()
        
        switch_to_current_player_window()
        if not page_contains_by_text('End turn'):
            raise Exception('No End turn after Mancato reaction from target')

        log_passed(test_name)
    except Exception as e:
        log_failed(test_name, e)
