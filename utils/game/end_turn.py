from selenium.webdriver.common.by import By
from utils.locators.page_contains import page_contains_by_text
from globals import driver

def end_turn():
    button = driver.find_elements(By.XPATH, "//*[contains(text(),'End turn')]")[0]
    button.click()
