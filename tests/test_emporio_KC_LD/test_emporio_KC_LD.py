from utils.game.end_turn import end_turn
from utils.game.get_draw_choice_card import get_draw_choice_card
from utils.game.get_emporio_card import get_emporio_card
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
from utils.locators.get_draw_choice_cards_length import get_draw_choice_cards_length
from utils.locators.get_draw_choice_cards_playable import get_draw_choice_cards_playable
from utils.locators.get_emporio_cards_length import get_emporio_cards_length
from utils.locators.get_emporio_cards_playable import get_emporio_cards_playable
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
from selenium.webdriver.common.by import By

def test_emporio_KC_LD():
    '''

    '''
    
    test_name = "Test Emporio, KC, LD"
    try:
        USERS[0] = "t_emporio_dnpauey"
        prepare_test()

        test_kit_carlson()

        use_card('Emporio')

        test_emporio()

        end_turn()

        test_LD()

    except Exception as e:
        log_failed(test_name, e)


def test_kit_carlson():
    switch_to_window(USERS[0])
    if page_contains_by_text('End turn'):
        raise Exception('Kit Carlson can end turn before card choice')
    if page_contains_by_text('Cancel'):
        raise Exception('Kit Carlson can cancel before card choice')
    
    get_draw_choice_card()
    if page_contains_by_text('End turn'):
        raise Exception('Kit Carlson can end turn before card choice')
    draw_choice = driver.find_elements(By.ID, "draw-choice-cards")[0]
    draw_choice_cards = draw_choice.find_elements(By.TAG_NAME, "button")
    if len(draw_choice_cards) != 2:
        raise Exception('Kit Carlson card not removed from draw choice')
    get_draw_choice_card()
    if not page_contains_by_text('End turn'):
        raise Exception('Kit Carlson cannot continue after getting choice cards')
    
    log_passed('Kit Carlson')

def test_emporio():
    if not get_emporio_cards_playable():
        raise Exception('Emporio cards not active')

    switch_to_window(USERS[1])
    if get_emporio_cards_playable():
        raise Exception('Emporio cards active')

    switch_to_window(USERS[0])
    current_num_of_cards_in_hand = get_num_of_cards_in_player_hand()
    get_emporio_card()
    if get_emporio_cards_playable():
        raise Exception('Emporio cards not active')
    if get_emporio_cards_length() != 1:
        raise Exception('Emporio card not removed')
    if get_num_of_cards_in_player_hand() - current_num_of_cards_in_hand != 1:   
        raise Exception('Emporio card not added to hand')
    if player_hand_contains_active_card('Bang!'):
        raise Exception('Player hand active when waiting on emporio')

    switch_to_window(USERS[1])
    current_num_of_cards_in_hand = get_num_of_cards_in_player_hand()
    get_emporio_card()
    if get_num_of_cards_in_player_hand() - current_num_of_cards_in_hand != 1:
        raise Exception('Emporio card not added to hand')
    switch_to_current_player_window()

    log_passed('Emporio')

def test_LD():
    if get_draw_choice_cards_length() != 2:
        raise Exception('Lucky Duke does not have 2 cards to choose')
    if not get_draw_choice_cards_playable():
        raise Exception('Lucky Duke draw choice not playable')
        
    current_num_of_cards_in_hand = get_num_of_cards_in_player_hand()
    get_draw_choice_card()
    if get_num_of_cards_in_player_hand() - current_num_of_cards_in_hand != 1:
        raise Exception('Lucky Duke did not receive card in hand after draw')
    if get_draw_choice_cards_length() != 2:
        raise Exception('Lucky Duke does not have 2 cards to choose')
    if not get_draw_choice_cards_playable():
        raise Exception('Lucky Duke draw choice not playable')
    
    get_draw_choice_card()
    if not player_hand_contains_active_card('Bang!'):
        raise Exception('Lucky Duke hand not playable after card choice')
    
    if not page_contains_by_text('End turn'):
        raise Exception('Lucky Duke cannot play after getting choice cards')
    
    log_passed('Lucky Duke')
    
