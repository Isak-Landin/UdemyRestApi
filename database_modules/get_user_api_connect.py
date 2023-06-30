from database_modules.localconfig import table_users, keyspace, admin_headers, astra_id
import requests
from flask import make_response, Response


def get_user(username, jwt_access=None, jwt_refresh=None):
    if jwt_access and jwt_refresh:
        # Add todo if necessary
        pass
    url = f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v1/keyspaces/{keyspace}/tables/{table_users}/rows/{username}'
    return requests.get(url, headers=admin_headers)

