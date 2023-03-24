from utils.window.switch_to_window_that_contains import switch_to_window_that_contains_text

def switch_to_current_player_window():
    return (switch_to_window_that_contains_text('End turn') or 
            switch_to_window_that_contains_text('Cancel'))