from selenium.webdriver.common.by import By
from globals import driver

def login_user(username: str):
    username_input =  driver.find_elements(By.ID,"username-input")[0]
    username_input.send_keys(username)

    button = driver.find_elements(By.XPATH, "//*[contains(text(),'Set username')]")[0]
    button.click()