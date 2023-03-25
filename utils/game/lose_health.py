from globals import driver
from selenium.webdriver.common.by import By

def lose_health():
    button = driver.find_elements(By.XPATH, "//*[contains(text(),'Lose health')]")[0]

    button.click()