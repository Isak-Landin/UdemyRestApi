from flask_jwt_extended import create_access_token, create_refresh_token
from typing import Tuple, Optional
import requests

from database_modules.users_table.get_user_api_connect import get_user_and_password
from database_modules.utils import response_content_decoder, get_data_in_dict, get_count_in_dict

import bcrypt


class Tokens:
    @staticmethod
    def _is_user_exist_in_response_internal(get_user_response: requests.Response) -> bool:
        if get_user_response:
            content_decoded = response_content_decoder(get_user_response)
            count = get_count_in_dict(content_decoded)
            return count > 0
        return False

    @staticmethod
    def _is_correct_password_internal(input_username: str, input_password: str, response: requests.Response) -> bool:
        decoded_response = response_content_decoder(response=response)
        decoded_data = get_data_in_dict(decoded_response)

        def _strip_field_internal(field):
            return decoded_data.get(field, '')

        stripped_password = _strip_field_internal('password')
        stripped_salt = _strip_field_internal('salt')
        if _strip_field_internal('username') == input_username:
            return bcrypt.checkpw(input_password.encode(), stripped_password.encode())
        return False

    @staticmethod
    def validate_user_login(username: str, password: str) -> bool:
        get_user_response = get_user_and_password(username=username)
        if isinstance(get_user_response, requests.Response) and \
                Tokens._is_user_exist_in_response_internal(
                    get_user_response=get_user_response
                ):
            return Tokens._is_correct_password_internal(
                input_username=username,
                input_password=password,
                response=get_user_response)
        return False

    @staticmethod
    def generate_token_pair(username: str = None,
                            password: str = None,
                            received_access_token: str = None,
                            received_refresh_token: str = None,
                            token_salt=None) -> Optional[Tuple[str, str]]:
        if username and password:
            if Tokens.validate_user_login(username, password):
                access_token = create_access_token(identity=username)
                refresh_token = create_refresh_token(identity=username)
                return access_token, refresh_token
        elif not username and not password and received_access_token and received_refresh_token:
            # Future code here
            pass


    @staticmethod
    def create_new_token_salt():
        pass


    @staticmethod
    def store_new_token_salt():
        pass
