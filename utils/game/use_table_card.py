from selenium.webdriver.common.by import By
from globals import driver

def use_table_card(card_name: str):
    player_table = driver.find_elements(By.ID, "player-table")[0]
    cards = player_table.find_elements(By.ID, card_name)
    if len(cards) == 0:
        raise Exception(f"No {card_name} on table")
    
    card = cards[0]
    card.click()