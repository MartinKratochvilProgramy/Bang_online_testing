from selenium.webdriver.common.by import By
from globals import driver

def get_num_of_cards_in_target_player_hand(username: str):
    player_hand = driver.find_elements(By.ID, "cards-" + username)[0]
    cards_in_hand = player_hand.find_elements(By.XPATH, ".//*")

    return len(cards_in_hand)