from globals import driver, USERS

def switch_to_window(username: str):
    index =  USERS.index(username)
    driver.switch_to.window(driver.window_handles[index])   