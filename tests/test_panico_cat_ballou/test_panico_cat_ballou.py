from utils.game.end_turn import end_turn
from utils.game.prepare_test import prepare_test
from utils.game.use_card import use_card
from utils.game.use_card_with_table_target import use_card_with_table_target
from utils.game.use_card_with_target import use_card_with_target
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand
from utils.locators.get_num_of_cards_in_target_player_hand import get_num_of_cards_in_target_player_hand
from utils.locators.get_num_of_cards_on_target_player_table import get_num_of_cards_on_target_player_table
from utils.logging.log_failed import log_failed
from utils.logging.log_passed import log_passed
from utils.window.switch_to_window import switch_to_window
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from globals import USERS

def test_panico_cat_ballou():
    '''
        CJ vs Jourdonnais
        CJ ha Barilo on table, uses CB on Jourd
        Jourd uses CB on Barilo
        Jourd uses Panico on CJ
        Jourd places Barilo on table
        CJ uses Panico on Barilo
    '''
    
    test_name = "Test Panico, Cat Ballou"
    try:
        USERS[0] = "t_panico_dnpauey"
        prepare_test()

        use_card('Barilo')

        test_cat_balou()
        test_panico()

    except Exception as e:
        log_failed(test_name, e)

def test_cat_balou():
    # Cat Ballou ON HAND CARD
    use_card_with_target('Cat Balou', USERS[1])
    
    if get_num_of_cards_in_target_player_hand(USERS[1]) != 3:
        raise Exception('Card not removed from oponents hand on Cat Balou')
    
    switch_to_window(USERS[1])
    
    if get_num_of_cards_in_player_hand() != 3:
        raise Exception('Card not removed from players hand on Cat Balou')
    
    switch_to_current_player_window()
    
    end_turn()
    
    # Cat Ballou ON TABLE CARD
    starting_cards_in_hand: int = get_num_of_cards_in_player_hand()
    starting_cards_on_table: int = get_num_of_cards_on_target_player_table(USERS[0])
    
    use_card_with_table_target('Cat Balou', USERS[0], 'Barilo')
    
    ending_cards_in_hand: int = get_num_of_cards_in_player_hand()
    ending_cards_on_table: int = get_num_of_cards_on_target_player_table(USERS[0])
    
    if starting_cards_in_hand - ending_cards_in_hand != 1:
        raise Exception(f"Cat Ballou not removed from hand when targeting player {USERS[0]}'s Barilo on table")
    if starting_cards_on_table - ending_cards_on_table != 1:
        raise Exception(f"Barilo not removed from table when {USERS[0]} was target of Cat Balou")

    log_passed('Cat Balou')

def test_panico():
    # PANICO ON HAND CARD
    starting_cards_in_hand: int = get_num_of_cards_in_player_hand()
    switch_to_window(USERS[0])
    oponent_starting_cards_in_hand: int = get_num_of_cards_in_player_hand()
    switch_to_current_player_window()

    use_card_with_target('Panico', USERS[0])
    
    ending_cards_in_hand: int = get_num_of_cards_in_player_hand()
    switch_to_window(USERS[0])
    oponent_ending_cards_in_hand: int = get_num_of_cards_in_player_hand()
    switch_to_current_player_window()

    if oponent_starting_cards_in_hand - oponent_ending_cards_in_hand != 1:
        raise Exception(f"Panico did not remove card from {USERS[0]}'s target hand")
    
    if starting_cards_in_hand - ending_cards_in_hand != 0:
        raise Exception(f"Card not received in hand when targeting Panico on {USERS[0]}")
    
    use_card('Barilo')
    end_turn()

    # PANICO ON TABLE CARD   
    starting_cards_in_hand: int = get_num_of_cards_in_player_hand()
    starting_cards_on_table: int = get_num_of_cards_on_target_player_table(USERS[1])
    
    use_card_with_table_target('Panico', USERS[1], 'Barilo')
    
    ending_cards_in_hand: int = get_num_of_cards_in_player_hand()
    ending_cards_on_table: int = get_num_of_cards_on_target_player_table(USERS[1])
    
    if starting_cards_in_hand - ending_cards_in_hand != 0:
        raise Exception(f"Panico not removed from hand when targeting player {USERS[1]}'s Barilo on table")
    if starting_cards_on_table - ending_cards_on_table != 1:
        raise Exception(f"Barilo not removed from table when {USERS[1]} was target of Panico")
    
    log_passed("Panico")