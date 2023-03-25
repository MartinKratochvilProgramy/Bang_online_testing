from selenium.webdriver.common.by import By
from globals import driver

def use_character():
    player_character = driver.find_elements(By.XPATH, '//img[@alt="Player character"]')[0]

    player_character.click()
