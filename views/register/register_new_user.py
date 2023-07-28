import flask

from database_modules.users_table import get_user_api_connect

from views.register.new_user_preparation import create_template
from GeneralUtils.decorators import standard_procedure

from flask import Response


def finalize_and_store_new_user() -> Response:
    # sourcery skip: inline-immediately-returned-variable
    response = Response()


    return response


@standard_procedure
def perform_initial_checks() -> bool:
    """
    :return: the returned bool will represent whether it's a green light.
    can the user be registered without collisions?
    :rtype: bool:
    """
    return False


@standard_procedure
def check_username_available(username: str):
    get_user_api_connect.get_user()

@standard_procedure
def create_template_and_user():
    pass