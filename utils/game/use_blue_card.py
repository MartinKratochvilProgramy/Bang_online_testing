from selenium.webdriver.common.by import By
from globals import driver
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand
from utils.locators.player_hand_contains import player_hand_contains
from utils.locators.player_table_contains import player_table_contains

def use_blue_card(card_name: str):
    starting_cards_in_hand: int = get_num_of_cards_in_player_hand()
    
    card = driver.find_elements(By.ID, card_name)[0]
    card.click()

    ending_cards_in_hand: int = get_num_of_cards_in_player_hand()

    if starting_cards_in_hand - ending_cards_in_hand != 1:
        raise Exception(f"Failed to remove {card_name} from hand")
    
    if not player_table_contains(card_name):
        raise Exception(f"Failed to put {card_name} onto table")
