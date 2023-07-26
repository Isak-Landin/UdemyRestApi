import requests
from database_modules.localconfig import astra_id, admin_headers, keyspace, table_emails


def get_email(email):
    url = f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v2/keyspaces/{keyspace}/{table_emails}/{email}'
    return requests.get(url, headers=admin_headers)