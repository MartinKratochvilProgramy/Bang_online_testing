from selenium import webdriver

ROUTE = "http://localhost:3000"
USERS = ["a", "b"]
# Create an instance of the webdriver (replace 'chromedriver' with the path to your Chrome webdriver executable)
driver = webdriver.Chrome('chromedriver')