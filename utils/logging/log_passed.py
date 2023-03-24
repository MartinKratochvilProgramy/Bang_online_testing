from utils.logging.colors import colors

def log_passed(test_name: str):
    print(colors.OKGREEN + f"PASSED: {test_name}" + colors.ENDC)