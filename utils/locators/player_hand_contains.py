from selenium.webdriver.common.by import By
from globals import driver

def player_hand_contains(card_name: str):
    player_hand = driver.find_elements(By.ID, "player-hand")[0]
    cards = player_hand.find_elements(By.ID, card_name)

    if len(cards) == 0:
        return False
    else: 
        return True 