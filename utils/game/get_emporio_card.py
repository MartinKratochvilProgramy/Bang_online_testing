from selenium.webdriver.common.by import By
from globals import driver

def get_emporio_card():
    draw_choice = driver.find_elements(By.ID, "draw-choice-emporio")[0]
    draw_choice_cards = draw_choice.find_elements(By.TAG_NAME, "button")

    draw_choice_cards[0].click()
    