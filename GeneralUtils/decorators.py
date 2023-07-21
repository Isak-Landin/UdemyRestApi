from functools import wraps
from flask import jsonify


def handle_exceptions(function):
    @wraps(function)
    def general_exception_message_event(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            error_response = {'error': str(e)}
            return jsonify(error_response), 500

    return general_exception_message_event
