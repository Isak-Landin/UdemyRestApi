import requests
import bcrypt
from database_modules.localconfig import astra_id, table_users, keyspace


def update_salt(username):
    new_token_salt = bcrypt.gensalt().decode('utf-8')
    url = f'{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v1/keyspaces/{keyspace}/tables/{table_users}/rows/{username}'

    body = {
        "changeset": [
            {
                "column": "token_salt",
                "value": f"{new_token_salt}"
            }
        ]
    }

    return requests.put(url, json=body)