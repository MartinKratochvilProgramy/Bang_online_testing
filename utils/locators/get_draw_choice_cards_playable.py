from selenium.webdriver.common.by import By
from globals import driver

def get_draw_choice_cards_playable() -> bool:
    draw_choice = driver.find_elements(By.ID, "draw-choice-cards")[0]
    draw_choice_cards = draw_choice.find_elements(By.TAG_NAME, "button")
    for card in draw_choice_cards:
        if card.value_of_css_property('border') != '2px solid rgb(255, 0, 0)':
            return False
        
    return True
    