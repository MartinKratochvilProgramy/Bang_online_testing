from selenium.webdriver.common.by import By
from globals import driver
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand

def activate_card(card_name: str):
    '''
        Similar to use_card() bot not with the discarding check
    '''
    player_hand = driver.find_elements(By.ID, "player-hand")[0]
    cards = player_hand.find_elements(By.ID, card_name)
    if len(cards) == 0:
        raise Exception(f"No {card_name} in hand")
    
    card = cards[0]
    card.click()