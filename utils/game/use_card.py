from selenium.webdriver.common.by import By
from utils.locators.page_contains import page_contains_by_text
from globals import driver

def use_card(card_name: str):
    cards = driver.find_elements(By.ID, card_name)
    if len(cards) == 0:
        raise Exception(f"No {card_name} in hand")
    
    card = cards[0]
    card.click()

    if len(cards) - len(driver.find_elements(By.ID, card_name)) != 1:
        raise Exception(f"On use_card: Number of {card_name}s in hand does not match")