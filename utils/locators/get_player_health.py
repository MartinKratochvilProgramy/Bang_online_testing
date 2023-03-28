from selenium.webdriver.common.by import By
from globals import driver

def get_player_health():
    player_health = driver.find_elements(By.ID, "player-health")[0]

    return int(player_health.text)

