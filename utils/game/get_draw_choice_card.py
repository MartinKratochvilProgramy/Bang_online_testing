from globals import driver
from selenium.webdriver.common.by import By

def get_draw_choice_card():
    draw_choice = driver.find_elements(By.ID, "draw-choice-cards")[0]
    draw_choice_cards = draw_choice.find_elements(By.TAG_NAME, "button")

    draw_choice_cards[0].click()