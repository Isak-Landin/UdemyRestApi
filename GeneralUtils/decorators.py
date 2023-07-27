from functools import wraps

import flask
from flask import jsonify, Response
from flask import request
import traceback

from flask_socketio import SocketIO, emit



def standard_procedure(function):
    @wraps(function)
    def standard_exception_return_event(*args, **kwargs):
        try:
            for arg in args:
                if isinstance(arg, flask.Response):
                    return arg
            for key, value in kwargs.items():
                if isinstance(value, Response):
                    return value
            return function(*args, **kwargs)
        except Exception as e:
            error_response = {
                'error': 'There was a server error that prevented your request from executing as expected. The error has been logged and we are working on a fix this very moment.',
                'direct-error': str(e)
            }
            print(traceback.format_exc())
            # TODO store this error in a database, figure out what columns are needed, pk and order to be stored

            return jsonify(error_response), 500

    return standard_exception_return_event