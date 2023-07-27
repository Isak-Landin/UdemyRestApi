import requests
from database_modules.localconfig import astra_id, keyspace, table_users, admin_headers


def get_token_salt(username):
    url = f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{table_users}/{username}?fields=token-salt'
    return requests.get(url, headers=admin_headers)