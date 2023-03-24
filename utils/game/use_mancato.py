from selenium.webdriver.common.by import By
from utils.locators.page_contains import page_contains_by_text
from globals import driver

def use_mancato():
    mancatos = driver.find_elements(By.ID, 'Mancato!')
    if len(mancatos) == 0:
        raise Exception('No Mancato! in hand')
    
    mancato = mancatos[0]
    mancato.click()

    if len(mancatos) - len(driver.find_elements(By.ID, 'Mancato!')) != 1:
        raise Exception('Number of Mancato!s in hand does not match')

    if page_contains_by_text('Lose health'):
        raise Exception('Player losing health after Mancato!')