from selenium.webdriver.common.by import By
from globals import driver

def create_room(room_name: str):
    room_name_input =  driver.find_elements(By.ID,"room-name-input")[0]
    room_name_input.send_keys(room_name)

    button = driver.find_elements(By.XPATH, "//*[contains(text(),'Create room')]")[0]
    button.click()