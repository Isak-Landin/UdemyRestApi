from functools import wraps
import traceback

import requests

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
    def standard_exception_return_event(*args, **kwargs):
        try:
            request_response: requests.Response = function(*args, **kwargs)
            request_response.raise_for_status()

            return request_response
        except Exception as e:
            print(traceback.format_exc())
            raise e

    return standard_exception_return_event
