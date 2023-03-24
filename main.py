# Import the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from login.login_all_users import login_all_users
from switch_to_window import switch_to_window
import time

ROUTE = "http://localhost:3000"
USERS = ["a", "b"]

if __name__ == '__main__':
    # Create an instance of the webdriver (replace 'chromedriver' with the path to your Chrome webdriver executable)
    driver = webdriver.Chrome('chromedriver')

    # Navigate to the webpage
    driver.get(ROUTE)

    login_all_users(USERS, ROUTE, driver)

    switch_to_window("a", USERS, driver)

    time.sleep(10)

    # Close the web window
    driver.quit()
