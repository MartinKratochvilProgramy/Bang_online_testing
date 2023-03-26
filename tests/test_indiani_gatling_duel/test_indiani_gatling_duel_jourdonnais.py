from utils.game.end_turn import end_turn
from utils.game.lose_health import lose_health
from utils.game.prepare_test import prepare_test
from utils.game.use_bang import use_bang
from utils.game.use_card import use_card
from utils.game.use_card_with_target import use_card_with_target
from utils.game.use_character import use_character
from utils.locators.character_active import character_active
from utils.locators.page_contains import page_contains_by_text
from utils.logging.log_failed import log_failed
from utils.logging.log_passed import log_passed
from utils.window.switch_to_window import switch_to_window
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from utils.locators.character_active import character_active
from utils.locators.player_hand_contains_active_card import player_hand_contains_active_card
from globals import driver, USERS

def test_indiani_gatling_duel_jourdonnais():
    '''
        CJ against Jourdonnais
        CJ uses Bang!, Jourdonnais active
        Jourdonnais draw hearts, all inactive
        CJ uses Gatling, Jourdonnais draws wrong -> use Mancato!
        Jourdonnais uses Indiani -> CJ reacts by using Mancato!
    '''
    test_name = "Test Indiani, Gatling, Duel, Jourdonnais"
    try:
        USERS[0] = "t_indiani_dnpauey"
        prepare_test()

        use_bang(USERS[1])
        switch_to_window(USERS[1])
        if not character_active("Jourdonnais"):
            raise Exception('Jourdonnais not active after Bang!') 
        use_character()
        if player_hand_contains_active_card('Mancato!'):
            raise Exception('Mancato still active after succesful Jourdonnais barel draw')
        log_passed('Jourdonnais')
        
        switch_to_current_player_window()
        use_card('Gatling')
        switch_to_window(USERS[1])
        if not page_contains_by_text('Lose health'):
            raise Exception('Player not losing health on Gatling')
        use_character()
        if character_active("Jourdonnais"):
            raise Exception('Jourdonnais still active after unsuccessful draw')
        use_card('Mancato!')
        log_passed('Gatling')

        switch_to_current_player_window()
        end_turn()

        use_card('Indiani')
        switch_to_window(USERS[0])
        if not page_contains_by_text('Lose health'):
            raise Exception('Player not losing health on Indiani')
        use_card('Mancato!')
        if player_hand_contains_active_card('Bang!') or player_hand_contains_active_card('Mancato!') or page_contains_by_text('Lose health'):
            raise Exception('Mancato! as Bang! does not resolve losing health on Indiani')
        log_passed('Indiani')

        # TEST DUEL
        switch_to_current_player_window()
        use_card_with_target('Duel', USERS[0])
        switch_to_window(USERS[0])

        # this also checks if CJ has Mancato!, for other players, remove the Mancato! active check
        if not player_hand_contains_active_card('Bang!') or not player_hand_contains_active_card('Mancato!') or not page_contains_by_text('Lose health'):
            raise Exception('Duel does not activate Losing health')
        use_card('Bang!')
        if player_hand_contains_active_card('Bang!'):
            raise Exception('Can still use Bang! in duel after Bang! reaction')

        switch_to_current_player_window()
        use_card('Bang!')
        if player_hand_contains_active_card('Bang!'):
            raise Exception('Can still use Bang! in duel after Bang! reaction')
        
        switch_to_window(USERS[0])
        lose_health()
        if page_contains_by_text('Lose health'):
            raise Exception('Player still losing health after Lose health press')
        log_passed('Duel')

    except Exception as e:
        log_failed(test_name, e)