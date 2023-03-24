from selenium.webdriver.common.by import By
from globals import driver

def page_contains_by_text(text: str)-> bool:
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(),'{text}')]")

    if len(elements) == 0:
        return False
    else:
        return True