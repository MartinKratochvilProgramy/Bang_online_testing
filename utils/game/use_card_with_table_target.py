from selenium.webdriver.common.by import By
from globals import driver
from utils.locators.get_num_of_cards_in_player_hand import get_num_of_cards_in_player_hand
from utils.locators.get_num_of_cards_on_target_player_table import get_num_of_cards_on_target_player_table

def use_card_with_table_target(card_name: str, target: str, target_card: str):
    '''
        target: name of target player eg. USERS[1]
        target_card: eg. Barilo
    '''
    cards = driver.find_elements(By.ID, card_name)
    if len(cards) == 0:
        raise Exception(f"No {card_name} in hand")
    
    card = cards[0]
    card.click()

    oponents_table = driver.find_elements(By.ID, "oponent-" + target + "-table")[0]
    found_card = oponents_table.find_elements(By.ID, target_card)[0]
    found_card.click()