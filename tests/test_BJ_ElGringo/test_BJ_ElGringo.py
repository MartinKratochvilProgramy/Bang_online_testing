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

def test_BJ_ElGringo():
    '''
    '''
    
    test_name = "Test BJ, ElGringo"
    try:
        USERS[0] = "t_BJ_ElG_dnpauey"
        prepare_test()

        if get_num_of_cards_in_player_hand() != 7:
            raise Exception('Black Jack did not receive extra card')
        
        log_passed('Black Jack')
        
        use_card_with_target('Bang!', USERS[1])
        switch_to_window(USERS[1])
        lose_health()
        switch_to_current_player_window()

        if get_num_of_cards_in_player_hand() != 5:
            raise Exception('El Gringo did not steal a card')
        
        switch_to_window(USERS[1])
        if get_num_of_cards_in_player_hand() != 4:
            raise Exception('El Gringo did receive the stolen card')

        log_passed('El Gringo')

    except Exception as e:
        log_failed(test_name, e)
