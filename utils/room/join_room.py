from selenium.webdriver.common.by import By
from globals import driver, USERS

def join_room():
    room = driver.find_elements(By.ID, USERS[0])[0]
    
    child_elements = room.find_elements(By.XPATH, "./*")

    # loop over the child elements and print their text content
    for child_element in child_elements:
        if child_element.text == "Join":
            child_element.click()