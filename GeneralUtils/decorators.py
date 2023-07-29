from functools import wraps
import traceback

def standard_procedure(function):
    @wraps(function)
    def standard_exception_return_event(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(traceback.format_exc())
            raise e
    return standard_exception_return_event


def request_procedure(function):
    @wraps(function)
    def standar