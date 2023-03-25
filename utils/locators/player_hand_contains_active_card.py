from globals import driver
from selenium.webdriver.common.by import By

def player_hand_contains_active_card(card_name: str):
    player_table = driver.find_elements(By.ID, "player-hand")[0]
    cards = player_table.find_elements(By.ID, card_name)[0]
    active_cards = cards.find_elements(By.XPATH, "//button[@style='cursor: pointer; color: red; border: 2px solid red;']")    
    
    if len(active_cards) == 0:
        return False
    else: 
        return True