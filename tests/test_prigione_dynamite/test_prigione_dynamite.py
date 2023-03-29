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

def test_prigione_dynamite():
    '''
        CJ vs JJ
        CJ places JJ to 2 prisons, draw 1 fails
        CJ places 2 dynamite on table, JJ draws prison, success, then failure
    '''
    
    test_name = "Test Prigione, Dynamite"
    try:
        USERS[0] = "t_prigione_dnpauey"
        prepare_test()

        use_card_with_target('Prigione', USERS[1])
        use_card_with_target('Prigione', USERS[1])

        end_turn()

        if player_hand_contains_active_card('Dynamite') or player_hand_contains_active_card('Prigione'):
            raise Exception('Hand active even though player in prison')
        
        if character_active('Jesse Jones'):
            raise Exception('Character active even though player in prison')

        # succesful draw #1
        use_table_card('Prigione')
        if player_hand_contains_active_card('Dynamite') or player_hand_contains_active_card('Prigione'):
            raise Exception('Hand active even though player in prison')
        if page_contains_by_text('End turn'):
            raise Exception('End turn active even though player in prison')
        
        # succesful draw #2
        use_table_card('Prigione')

        if page_contains_by_text('End turn'):
            raise Exception('End turn active before JJ draws')
        use_deck_card()
        
        use_card_with_target('Prigione', USERS[0])

        use_card('Dynamite')
        use_card('Dynamite')
        use_card('Dynamite')

        end_turn()
        switch_to_window(USERS[0])
        use_table_card('Prigione')
        if page_contains_by_text('End turn'):
            raise Exception('End turn active even though player failed prison')
        if player_hand_contains_active_card('Dynamite'):
            raise Exception('Hand active even though player failed prison')
        
        log_passed('Prigione')

        switch_to_window(USERS[1])

        use_table_card('Dynamite')
        use_table_card('Dynamite')
        use_table_card('Dynamite')
        
        if page_contains_by_text('End turn'):
            raise Exception('End turn active before JJ draws')
        use_deck_card()

        if get_player_health() != 1:
            raise Exception('Dynamite did not decrease helth by 3')
        log_passed('Lose health')
        
        end_turn()
        switch_to_window(USERS[0])

        use_table_card('Dynamite')
        use_table_card('Dynamite')

        end_turn()
        switch_to_window(USERS[1])

        use_table_card('Dynamite')
        if not page_contains_by_text('LEAVE ROOM'):
            raise Exception('Page does not contain LEAVE ROOM on player death')

        log_passed('Dynamite')        

        switch_to_window(USERS[0])
        if not page_contains_by_text('LEAVE ROOM'):
            raise Exception('Page does not contain LEAVE ROOM on player death')

        log_passed('Player death')        

    except Exception as e:
        log_failed(test_name, e)
