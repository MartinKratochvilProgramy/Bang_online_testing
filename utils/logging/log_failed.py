from utils.logging.colors import colors

def log_failed(test_name: str, exception: Exception):
    print(colors.FAIL + f"FAILED: {test_name}" + colors.ENDC)
    print(exception)