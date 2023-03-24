from globals import *
from selenium.webdriver.common.by import By

def start_game():
    button = driver.find_elements(By.XPATH, "//*[contains(text(),'START GAME')]")[0]
    button.click()