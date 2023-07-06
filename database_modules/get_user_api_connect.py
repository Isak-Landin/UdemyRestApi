import json

from database_modules.localconfig import table_users, keyspace, admin_headers, astra_id
from database_modules.utils import response_decoder
import requests
from flask import make_response, Response


def get_user_and_password(username):
    url = f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{table_users}/{username}?fields=username%2C%20password'
    return requests.get(url, headers=admin_headers)
