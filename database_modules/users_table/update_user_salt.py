import requests
import bcrypt
from database_modules.localconfig import astra_id, table_users, keyspace

from GeneralUtils.decorators import request_procedure


@request_procedure
def update_salt(username, salt):
    url = f'{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v1/keyspaces/{keyspace}/tables/{table_users}/rows/{username}'

    body = {
        "changeset": [
            {
                "column": "token-salt",
                "value": f"{salt}"
            }
        ]
    }

    return requests.put(url, json=body)