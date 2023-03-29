from utils.game.activate_card import activate_card
from utils.game.end_turn import end_turn
from utils.game.lose_health import lose_health
from utils.game.prepare_test import prepare_test
from utils.game.use_card import use_card
from utils.game.use_card_with_target import use_card_with_target
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand
from utils.locators.get_oponent_is_active import get_oponent_is_active
from utils.logging.log_failed import log_failed
from utils.logging.log_passed import log_passed
from utils.window.switch_to_window import switch_to_window
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from globals import USERS

def test_distances():
    '''
        USERS[0] - Rose Doolan
        USERS[1] - Paul Regret
        USERS[2] - Willy the Kid
        USERS[3] - Vulture Sam
    '''
    
    test_name = "Test distances"
    try:
        USERS[0] = "t_distances_dnpauey"
        USERS.append('c')
        USERS.append('d')
        
        prepare_test()

        activate_card('Bang!')
        if not get_oponent_is_active(USERS[1]) or not get_oponent_is_active(USERS[2]) or not get_oponent_is_active(USERS[3]):
            raise Exception('Player not in range')
        
        use_card_with_target('Bang!', USERS[1])
        switch_to_window(USERS[1])
        lose_health()
        switch_to_current_player_window()
        end_turn()
        end_turn()

        activate_card('Bang!')
        if get_oponent_is_active(USERS[1]):
            raise Exception('Paul Regret in range')
        use_card('Apaloosa')
        use_card('Mustang')
        activate_card('Bang!')
        if not get_oponent_is_active(USERS[1]):
            raise Exception('Apaloosa not helps with range')
        log_passed('Horses')

        use_card_with_target('Bang!', USERS[1])
        switch_to_window(USERS[1])
        lose_health()
        switch_to_current_player_window()
        end_turn()

        activate_card('Bang!')
        if get_oponent_is_active(USERS[1]):
            raise Exception('Paul Regret in range')
        if get_oponent_is_active(USERS[2]):
            raise Exception('Player with Mustang in range')
        use_card('Winchester')
        activate_card('Bang!')
        if not get_oponent_is_active(USERS[1]) or not get_oponent_is_active(USERS[2]):
            raise Exception('Winchester did not help with ranges')
        log_passed('Guns')

        use_card_with_target('Bang!', USERS[1])
        current_num_of_cards_in_hand = get_num_of_cards_in_player_hand()
        switch_to_window(USERS[1])
        dying_player_cards_in_hand = get_num_of_cards_in_player_hand()
        lose_health()
        switch_to_current_player_window()
        if get_num_of_cards_in_player_hand() != current_num_of_cards_in_hand + dying_player_cards_in_hand:
            raise Exception('Vulture Sam did not receive dying players cards')

        log_passed('Vulture Sam')

    except Exception as e:
        log_failed(test_name, e)
