import requests
import json
from database_modules.localconfig import admin_headers, astra_id


file = 'users\\users_db_current_structure.json'

headers = admin_headers

try:
    with open(file) as file:
        data = json.load(file)
except (FileNotFoundError| FileExistsError) as e:
    data = None

if data:
    body = data

    response = requests.post(
        f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v1/keyspaces/restapi/tables',
        headers=headers,
        json=data
    )

    print(response.content)
    print(response.status_code)