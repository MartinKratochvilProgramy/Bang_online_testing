def open_new_window(route: str, driver):
    # open the link in a new tab
    driver.execute_script("window.open('" + route + "', '_blank');")
    # switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
    # do something on the new tab, e.g. navigate to a different URL
    driver.get(route)