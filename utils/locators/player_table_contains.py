from selenium.webdriver.common.by import By
from globals import driver

def player_table_contains(card_name: str):
    player_table = driver.find_elements(By.ID, "player-table")[0]
    cards = player_table.find_elements(By.ID, card_name)

    if len(cards) == 0:
        return False
    else: 
        return True