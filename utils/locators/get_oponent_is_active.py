from selenium.webdriver.common.by import By
from globals import driver

def get_oponent_is_active(oponent_name: str) -> bool:
    '''
        oponent_name: USERS[0] etc.
    '''
    character_img = driver.find_elements(By.ID, 'oponent-' + oponent_name)[0]
    return character_img.get_attribute("style") == 'color: red; border: 2px solid red; cursor: pointer;'
