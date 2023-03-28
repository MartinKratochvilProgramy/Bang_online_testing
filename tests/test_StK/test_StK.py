from utils.game.end_turn import end_turn
from utils.game.lose_health import lose_health
from utils.game.prepare_test import prepare_test
from utils.game.use_bang import use_bang
from utils.game.use_card import use_card
from utils.game.use_card_with_table_target import use_card_with_table_target
from utils.game.use_card_with_target import use_card_with_target
from utils.game.use_character import use_character
from utils.game.use_deck_card import use_deck_card
from utils.game.use_table_card import use_table_card
from utils.locators.character_active import character_active
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand
from utils.locators.get_num_of_cards_in_target_player_hand import get_num_of_cards_in_target_player_hand
from utils.locators.get_num_of_cards_on_target_player_table import get_num_of_cards_on_target_player_table
from utils.locators.get_player_health import get_player_health
from utils.locators.page_contains import page_contains_by_text
from utils.logging.log_failed import log_failed
from utils.logging.log_passed import log_passed
from utils.window.switch_to_window import switch_to_window
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from utils.locators.character_active import character_active
from utils.locators.player_hand_contains_active_card import player_hand_contains_active_card
from globals import driver, USERS

def test_StK():
    '''
        CJ vs JJ
        CJ places JJ to 2 prisons, draw 1 fails
        CJ places 2 dynamite on table, JJ draws prison, success, then failure
    '''
    
    test_name = "Test Panico, Cat Ballou"
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
