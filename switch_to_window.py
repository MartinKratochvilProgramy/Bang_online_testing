def switch_to_window(username: str, users, driver):
    index =  users.index(username)
    driver.switch_to.window(driver.window_handles[index])   