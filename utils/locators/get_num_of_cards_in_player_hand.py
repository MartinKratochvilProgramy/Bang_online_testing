from selenium.webdriver.common.by import By
from globals import driver

def get_num_of_cards_in_player_hand():
    player_hand = driver.find_elements(By.ID, "player-hand")[0]
    cards_in_hand = player_hand.find_elements(By.TAG_NAME, "button")

    return len(cards_in_hand)