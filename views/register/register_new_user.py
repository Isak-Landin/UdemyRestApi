"""Flask Modules"""
from typing import Tuple, Any

import flask
from flask import Response

"""Database Modules"""
from database_modules.users_table.add_new_user import add_user
from database_modules.users_table.get_user_api_connect import get_user
from database_modules.mails_table.get_mail_api_connect import get_email
from database_modules.utils import response_content_decoder, get_count_in_dict

"""Other Modules"""
from views.register.new_user_preparation import create_template
from GeneralUtils.decorators import standard_procedure


def finalize_and_store_new_user(username, mail, password) -> Response:
    # sourcery skip: inline-immediately-returned-variable
    response = Response()

    is_username_available, is_mail_available = perform_initial_checks(username, mail)
    if all((is_username_available, is_mail_available)):
        template_for_new_user = create_template_for_user(username, mail, password)
        store_new_user(template_for_new_user)

        response.status_code = 201
        response.response = {'msg': 'New user registered', 'mail': 'available', 'username': 'available'}
    elif is_username_available and not is_mail_available:
        response.status_code = 200
        response.response = {'msg': 'Mail is busy', 'mail': 'busy', 'username': 'available'}
    elif not is_username_available and is_mail_available:
        response.status_code = 200
        response.response = {'msg': 'Username is busy', 'mail': 'available', 'username': 'busy'}
    else:
        response.status_code = 200
        response.response = {'msg': 'Mail and username are busy', 'mail': 'busy', 'username': 'busy'}
    return response


@standard_procedure
def store_new_user(request_body) -> None:
    print('This is the printed request_body')
    print(request_body)
    add_user(request_body)

@standard_procedure
def perform_initial_checks(username, mail) -> tuple[bool, bool]:
    """
    :return: the returned bool will represent whether it's a green light.
    can the user be registered without collisions?
    :rtype: bool:
    """

    is_username_available = check_username_available(username)
    is_mail_available = check_mail_available(mail)

    return is_username_available, is_mail_available


@standard_procedure
def check_username_available(username: str) -> bool:
    username_in_database_response = get_user(username)
    decoded_response_content = response_content_decoder(username_in_database_response)
    count = get_count_in_dict(decoded_response_content)

    return count == 0


@standard_procedure
def check_mail_available(mail) -> bool:
    mail_in_database_response = get_email(mail)
    decoded_response_content = response_content_decoder(mail_in_database_response)
    count = get_count_in_dict(decoded_response_content)

    return count == 0
@standard_procedure
def create_template_for_user(username, mail, password) -> dict:
    return create_template(username, mail, password)