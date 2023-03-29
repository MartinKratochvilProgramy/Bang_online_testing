from selenium.webdriver.common.by import By
from globals import driver

def use_deck_card():
    deck_card = driver.find_elements(By.XPATH, '//img[@alt="deck card"]')[0]
    if deck_card.value_of_css_property('border') != '2px solid rgb(255, 0, 0)':
        raise Exception('Deck not active')
    deck_card.click()
    