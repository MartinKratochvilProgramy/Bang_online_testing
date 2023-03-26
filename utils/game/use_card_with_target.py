from selenium.webdriver.common.by import By
from globals import driver

def use_card_with_target(card_name: str, target: str):
    '''
        target: name of target player eg. USERS[1]
    '''
    cards = driver.find_elements(By.ID, card_name)
    if len(cards) == 0:
        raise Exception(f"No {card_name} in hand")
    
    card = cards[0]
    card.click()

    oponent = driver.find_elements(By.ID, "oponent-" + target)[0]
    oponent.click()