import requests
from database_modules.get_user_api_connect import get_user
import json
import contextlib


def validate_user(username: str, password: str, secret=None) -> bool:
    is_user_response = get_user(username=username)

    if is_user_exist_in_response(is_user_response=is_user_response):
        is_correct_password(password=password)


def is_user_exist_in_response(is_user_response: requests.Response) -> bool:
    is_username = False
    if is_user_response:
        with contextlib.suppress(AttributeError, TypeError, KeyError):
            content_decoded = json.loads(is_user_response.content.decode('utf-8'))
            count = content_decoded['count']
            if count > 0:
                is_username = True

    return is_username


def is_correct_password(password: str):
    pass

test_value_dict = validate_user(username='test', password='test')

