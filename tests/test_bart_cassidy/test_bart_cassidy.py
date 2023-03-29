from utils.game.lose_health import lose_health
from utils.game.prepare_test import prepare_test
from utils.game.use_card_with_target import use_card_with_target
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand
from utils.logging.log_failed import log_failed
from utils.logging.log_passed import log_passed
from utils.window.switch_to_window import switch_to_window
from globals import USERS

def test_bart_cassidy():
    '''
        Bart Cassidy takes a hit
    '''
    
    test_name = "Test Bart Cassidy"
    try:
        USERS[0] = "t_bart_dnpauey"
        prepare_test()

        use_card_with_target('Bang!', USERS[1])

        switch_to_window(USERS[1])
        current_num_of_cards_in_hand = get_num_of_cards_in_player_hand()
        lose_health()

        if get_num_of_cards_in_player_hand() - current_num_of_cards_in_hand != 1:
            raise Exception('Bart Cassidy did not draw a card on being hit')

        log_passed('Bart Cassidy')

    except Exception as e:
        log_failed(test_name, e)
