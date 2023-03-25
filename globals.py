from selenium import webdriver

ROUTE = "http://localhost:3000"
USERS = ["t_bang_dnpaueyIPoew", "b"]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# Create an instance of the webdriver (replace 'chromedriver' with the path to your Chrome webdriver executable)
driver = webdriver.Chrome('chromedriver', options=options)