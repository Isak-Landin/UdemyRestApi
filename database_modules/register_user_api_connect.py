from database_modules.localconfig import admin_headers, admin_token, astra_id, table_users
from database_modules.get_user_api_connect import get_user, get_email
from database_modules.utils import response_decoder
import requests


def register_new_user(username, email, password):
    if not is_username_or_email_exists(username, email):
        pass


def is_username_or_email_exists(username, email) -> bool:
    response_is_email = get_email(email=email)
    response_is_user = get_user(username=username)
    return False