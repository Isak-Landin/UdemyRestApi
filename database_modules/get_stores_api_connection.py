import requests
from database_modules.localconfig import astra_id, admin_headers, keyspace, table_stores
from flask import make_response, Response


def get_items(store):
    url = f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v1/keyspaces/{keyspace}/tables/{table_stores}/rows/{store}'
    response = requests.get(url, headers=admin_headers)
    try:
        flask_response = make_response(response.content)
        flask_response.status_code = response.status_code
        flask_response.headers['Content-Type'] = response.headers.get('Content-Type')
    except Exception as e:
        print(e)
        flask_response = Response()

    return flask_response

