"""Flask Modules"""
import flask
from flask import Response

"""Database Modules"""
from database_modules.users_table.get_user_api_connect import get_user

"""Other Modules"""
from views.register.new_user_preparation import create_template
from GeneralUtils.decorators import standard_procedure
from database_modules.utils import response_content_decoder, get_count_in_dict


def finalize_and_store_new_user() -> Response:
    # sourcery skip: inline-immediately-returned-variable
    response = Response()


    return response


@standard_procedure
def perform_initial_checks(username, mail) -> bool:
    """
    :return: the returned bool will represent whether it's a green light.
    can the user be registered without collisions?
    :rtype: bool:
    """

    is_username_available = check_username_available(username)
    return False


@standard_procedure
def check_username_available(username: str):
    username_in_database_response = get_user(username)
    decoded_response_content = response_content_decoder(username_in_database_response)
    count = get_count_in_dict(decoded_response_content)

    return count == 0


@standard_procedure
def check_mail_available(mail):
    mail_in_database_response =
@standard_procedure
def create_template_and_user():
    pass