from selenium.webdriver.common.by import By
from globals import driver

def get_num_of_cards_on_target_player_table(username: str):
    player_table = driver.find_elements(By.ID, "oponent-" + username + "-table")[0]
    cards_on_table = player_table.find_elements(By.TAG_NAME, "button")

    return len(cards_on_table)