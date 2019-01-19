import traceback

from entsoe.exceptions import NoMatchingDataError


def handle_errors(func):
    try:
        return func()
    except NoMatchingDataError as e:
        print("NoMatchingDataError")
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    return None
