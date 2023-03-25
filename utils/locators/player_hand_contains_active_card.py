from globals import driver
from selenium.webdriver.common.by import By

def player_hand_contains_active_card(card_name: str):
    player_table = driver.find_elements(By.ID, "player-hand")[0]

    cards = player_table.find_elements(By.ID, card_name)
    for card in cards:
        if (card.get_attribute("style") == 'color: red; border: 2px solid red; cursor: pointer;'):
            return True
        
    return False