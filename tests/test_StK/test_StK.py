from utils.game.end_turn import end_turn
from utils.game.prepare_test import prepare_test
from utils.game.use_card import use_card
from utils.game.use_card_with_target import use_card_with_target
from utils.game.use_character import use_character
from utils.game.use_table_card import use_table_card
from utils.locators.page_contains import page_contains_by_text
from utils.logging.log_failed import log_failed
from utils.logging.log_passed import log_passed
from utils.window.switch_to_window import switch_to_window
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from utils.locators.player_hand_contains_active_card import player_hand_contains_active_card
from globals import USERS

def test_StK():
    '''
        StK vs Jourd
    '''
    
    test_name = "Test StK"
    try:
        USERS[0] = "t_StK_dnpauey"
        prepare_test()

        use_card_with_target('Bang!', USERS[1])

        switch_to_window(USERS[1])
        use_card('Mancato!')
        if not page_contains_by_text('Lose health'):
            raise Exception('Player not losing health after 1 Mancato! on StK')
        if not player_hand_contains_active_card('Mancato!'):
            raise Exception('Player hand not active after 1 Mancato! on StK')
        use_card('Mancato!')
        if page_contains_by_text('Lose health'):
            raise Exception('Player still losing health after 2 Mancato! on StK')
        
        switch_to_current_player_window()
        end_turn()

        use_card('Barilo')
        end_turn()

        use_card_with_target('Bang!', USERS[1])

        switch_to_window(USERS[1])
        use_character()
        use_table_card('Barilo')
        if page_contains_by_text('Lose health'):
            raise Exception('Player still losing health after Jourdonnais and Barilo draw on StK')
        
        log_passed('Slab the Killer')

    except Exception as e:
        log_failed(test_name, e)
