from utils.logging.colors import colors
import traceback

def log_failed(test_name: str, exception: Exception):
    print(colors.FAIL + f"FAILED: {test_name}" + colors.ENDC)
    print(''.join(traceback.format_exception(etype=type(exception), value=exception, tb=exception.__traceback__)))