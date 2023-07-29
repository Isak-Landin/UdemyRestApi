import json

from database_modules.localconfig import table_users, table_emails, keyspace, admin_headers, astra_id
from database_modules.utils import response_content_decoder
import requests
from flask import make_response, Response

from GeneralUtils.decorators import request_procedure


@request_procedure
def get_user_and_password(username):
    url = f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{table_users}/{username}?fields=username%2C%20password'
    return requests.get(url, headers=admin_headers)


@request_procedure
def get_user(username) -> requests.Response:
    """
    Retrieves the column username from the row that matches the parameter username as a primary key.
    The row is embedded in a requests.Response

    :param username:
    :type: str:
    :rtype: requests.Response
    """
    url = f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{table_users}/{username}?fields=username'
    return requests.get(url, headers=admin_headers)