import requests
from database_modules.localconfig import astra_id, admin_headers, table_users, keyspace

from GeneralUtils.decorators import request_procedure


@request_procedure
def add_user(body) -> None:
    url = f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v1/keyspaces/{keyspace}/tables/{table_users}/rows'
    requests.post(url, headers=admin_headers, data=body)

