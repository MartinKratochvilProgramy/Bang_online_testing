from selenium.webdriver.common.by import By
from globals import driver
from utils.window.switch_to_current_player_window import switch_to_current_player_window

def end_turn():
    end_turn_button = driver.find_elements(By.XPATH, "//*[contains(text(),'End turn')]")[0]
    end_turn_button.click()

    while True:
        end_turn_button = driver.find_elements(By.XPATH, "//*[contains(text(),'End turn')]")
        if len(end_turn_button) != 0:
            player_hand = driver.find_elements(By.ID, "player-hand")[0]
            first_card_in_hand = player_hand.find_elements(By.TAG_NAME, "button")[0]
            first_card_in_hand.click()
        else:
            switch_to_current_player_window()
            return



