from selenium.webdriver.common.by import By
from utils.locators.page_contains import page_contains_by_text
from globals import driver

def use_bang(target):
    bangs = driver.find_elements(By.ID, 'Bang!')
    if len(bangs) == 0:
        raise Exception('No Bang! in hand')
    
    bang = bangs[0]
    bang.click()

    oponent = driver.find_elements(By.ID, f"oponent-{target}")[0]
    oponent.click()

    if len(bangs) - len(driver.find_elements(By.ID, 'Bang!')) != 1:
        raise Exception('Number of Bang!s in hand does not match')
    
    if page_contains_by_text('End turn'):
        raise Exception('Can continue playing after using Bang!')
