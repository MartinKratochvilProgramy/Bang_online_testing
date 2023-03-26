from selenium.webdriver.common.by import By
from globals import driver
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand

def use_card(card_name: str):
    starting_cards_in_hand: int = get_num_of_cards_in_player_hand()
    player_hand = driver.find_elements(By.ID, "player-hand")[0]
    cards = player_hand.find_elements(By.ID, card_name)
    if len(cards) == 0:
        raise Exception(f"No {card_name} in hand")
    
    card = cards[0]
    card.click()

    ending_cards_in_hand: int = get_num_of_cards_in_player_hand()

    if starting_cards_in_hand - ending_cards_in_hand != 1:
        raise Exception(f"On use_card: Number of {card_name}s in hand does not match")