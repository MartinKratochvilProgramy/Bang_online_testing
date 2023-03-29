from utils.game.lose_health import lose_health
from utils.game.prepare_test import prepare_test
from utils.game.use_card_with_target import use_card_with_target
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand
from utils.logging.log_failed import log_failed
from utils.logging.log_passed import log_passed
from utils.window.switch_to_window import switch_to_window
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from globals import USERS

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
