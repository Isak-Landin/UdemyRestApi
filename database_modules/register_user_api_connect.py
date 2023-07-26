from database_modules.localconfig import admin_headers, admin_token, astra_id, table_users
from database_modules.get_user_api_connect import get_user
from database_modules.get_mail_api_connect import get_email
from database_modules.utils import response_content_decoder, get_count_in_dict, get_status_code_of_response
import requests


def save_user_to_database(username, email):
    if not is_username_or_email_exists(username, email):
        pass


def is_username_or_email_exists(username, email) -> bool:
    retrieved_email_response = get_email(email=email)
    retrieved_username_response = get_user(username=username)

    if get_status_code_of_response(retrieved_username_response) == 200 and get_status_code_of_response(retrieved_email_response) == 200:
        is_username = get_count_in_dict(response_content_decoder(retrieved_username_response))
        is_email = get_count_in_dict(response_content_decoder(retrieved_email_response))

        if is_username == 0 and is_email == 0:
            return False

    return True