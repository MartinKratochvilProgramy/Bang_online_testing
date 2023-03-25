from selenium.webdriver.common.by import By
from globals import driver

def character_active(character_name: str):
    character_img = driver.find_elements(By.ID, character_name)[0]
    if (character_img.get_attribute("style") == 'border: 2px solid red; cursor: pointer;'):
        return True
    else: 
        return False