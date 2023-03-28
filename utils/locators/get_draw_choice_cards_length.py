from selenium.webdriver.common.by import By
from globals import driver

def get_draw_choice_cards_length() -> int:
    draw_choice = driver.find_elements(By.ID, "draw-choice-cards")[0]
    draw_choice_cards = draw_choice.find_elements(By.TAG_NAME, "button")

    return len(draw_choice_cards)
    