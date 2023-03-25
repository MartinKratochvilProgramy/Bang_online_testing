from utils.login.login_all_users import login_all_users
from utils.room.join_room_all_users import join_room_all_users
from utils.start_game.pick_characters import pick_characters
from utils.start_game.start_game import start_game
from utils.window.switch_to_current_player_window import switch_to_current_player_window
from globals import driver, ROUTE

def prepare_test():
    # reset all windows to ROUTE
    for window in driver.window_handles:
        driver.switch_to.window(window)
        driver.get(ROUTE) 
    driver.switch_to.window(driver.window_handles[0])
    
    login_all_users()
    join_room_all_users()
    start_game()
    pick_characters()
    switch_to_current_player_window()
