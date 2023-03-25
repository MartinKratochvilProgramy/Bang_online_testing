from tests.test_bang_mancato_barilo_vulcanic_CJ_WtK.test_login import test_login
from tests.test_bang_mancato_barilo_vulcanic_CJ_WtK.test_join_room import test_join_room
from tests.test_bang_mancato_barilo_vulcanic_CJ_WtK.test_start_game import test_start_game
from utils.logging.log_passed import log_passed
from utils.logging.log_failed import log_failed
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from utils.window.switch_to_window import switch_to_window
from utils.game.use_blue_card import use_blue_card
from utils.game.use_bang import use_bang
from utils.game.use_mancato import use_mancato
from utils.game.use_card import use_card
from utils.game.use_table_card import use_table_card
from utils.game.end_turn import end_turn
from utils.locators.player_table_contains_active_card import player_table_contains_active_card
from utils.locators.player_hand_contains_active_card import player_hand_contains_active_card
from utils.locators.page_contains import page_contains_by_text
from globals import *

def test_bang_mancato_barilo_vulcanic_CJ_WtK():
    test_name = "Test Bang!, Mancato!, Barilo, Vulcanic, CJ, WtK"
    try:
        test_login()
        test_join_room()
        test_start_game()

        switch_to_current_player_window()
        
        use_blue_card('Barilo')

        # USE BANG! #1
        use_bang(USERS[1])
        switch_to_window(USERS[1])
        if not page_contains_by_text('Lose health'):
            raise Exception('Target not losing health after Bang!')
        use_mancato()
        
        switch_to_current_player_window()
        
        # USE VULCANIC, RESET BANG!
        use_blue_card('Vulcanic')

        # USE BANG! #2
        use_bang(USERS[1])
        switch_to_window(USERS[1])
        if not page_contains_by_text('Lose health'):
            raise Exception('Target not losing health after Bang!')
        use_mancato()
        
        switch_to_current_player_window()
        
        end_turn()
        switch_to_current_player_window()
        use_bang(USERS[0])
        switch_to_window(USERS[0])
        if not player_table_contains_active_card('Barilo'):
            raise Exception('Barel not active on Bang!')
        
        use_table_card('Barilo')
        if player_table_contains_active_card('Barilo'):
            raise Exception('Barel active after drawing hearts')
        if page_contains_by_text('Lose health'):
            raise Exception('Player losing health after success on Barel')
        
        switch_to_current_player_window()
        use_bang(USERS[0])
        switch_to_window(USERS[0])

        if not player_hand_contains_active_card('Bang!'):
            raise Exception('Bang! not active after CJ got hit by Bang!')
        if not player_hand_contains_active_card('Mancato!'):
            raise Exception('Mancato! not active on Bang!')

        use_card('Bang!') # CJ uses Bang! as Mancato!
        if player_table_contains_active_card('Barilo'):
            raise Exception('Barel does not deactivate on Bang! as Mancato!')
        if page_contains_by_text('Lose health'):
            raise Exception('Player losing health after playing Mancato!')

        switch_to_current_player_window()

        log_passed(test_name)
    except Exception as e:
        log_failed(test_name, e)