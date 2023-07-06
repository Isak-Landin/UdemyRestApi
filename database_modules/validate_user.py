import requests

from database_modules.get_user_api_connect import get_user_and_password
from database_modules.localconfig import astra_id, keyspace, table_users
from database_modules.utils import response_decoder, get_data_in_dict, get_rows_in_dict, get_count_in_dict

import bcrypt
import json
import contextlib


def validate_user(username: str, password: str) -> bool:
    get_user_response = get_user_and_password(username=username)
    print('Username, password retrieved from client-request: ', username, password)
    print('Database values for the client request: ', get_user_response, get_user_response.content)

    if isinstance(get_user_response, requests.Response) and \
            is_user_exist_in_response(get_user_response=get_user_response):
        print('Is request.Response, is user exists in db response')
        return is_correct_password(input_username=username, input_password=password, response=get_user_response)

    return False


def is_user_exist_in_response(get_user_response: requests.Response) -> bool:
    is_username = False
    if get_user_response:
        content_decoded = response_decoder(get_user_response)
        count = get_count_in_dict(content_decoded)
        try:
            if count > 0:
                is_username = True
        except TypeError:
            with contextlib.suppress(TypeError):
                if int(count) > 0:
                    is_username = True

    return is_username


def is_correct_password(input_username: str, input_password: str, response: requests.Response) -> bool:
    decoded_response = response_decoder(response=response)
    decoded_data = get_data_in_dict(decoded_response)

    def strip_password():
        if decoded_data:
            password = decoded_data.get('password')
            if password:
                return password

        return ''

    def strip_username():
        if decoded_data:
            username = decoded_data.get('username')
            if username:
                return username

        return ''

    def strip_salt():
        if decoded_data:
            salt = decoded_data.get('salt')
            if salt:
                return salt

        return ''

    def bcrypt_match_passwords(stripped_response_password: str, stripped_response_salt: str):
        if not bool(stripped_response_password) or not bool(stripped_response_salt):
            return False

        print('Passes bcrypt methods return check')

        print('Stripped salt: ', stripped_response_salt)
        print('Input password: ', input_password)
        print('Hashed stripped password: ', stripped_response_password)
        is_valid_password = bcrypt.checkpw(input_password.encode(), stripped_response_password.encode())

        print('Password validity: ', is_valid_password)
        return is_valid_password

    stripped_password = strip_password()
    stripped_salt = strip_salt()
    print('Stripped password: ', stripped_password)
    print('Stripped salt: ', stripped_salt)
    if strip_username() == input_username:
        return bcrypt_match_passwords(stripped_response_password=stripped_password, stripped_response_salt=stripped_salt)

    return False
