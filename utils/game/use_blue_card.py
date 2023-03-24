from selenium.webdriver.common.by import By
from globals import driver
from utils.locators.player_hand_contains import player_hand_contains
from utils.locators.player_table_contains import player_table_contains

def use_blue_card(card_name: str):
    card = driver.find_elements(By.ID, card_name)[0]
    card.click()

    if player_hand_contains(card_name):
        raise Exception(f"Failed to remove {card_name} from hand")
    
    if not player_table_contains(card_name):
        raise Exception(f"Failed to put {card_name} onto table")
