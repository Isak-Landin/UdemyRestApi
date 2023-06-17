import requests
import json
from database_modules.localconfig import admin_token, astra_id, admin_headers


def format_and_change_values(original_json, *args):
    column_list = original_json['columns']
    index = 0
    if len(args) == len(column_list):
        for column in column_list:
            column['value'] = args[index]
            index += 1
    elif len(args) < 2:
        raise ValueError('Expected to get at least 2 arguments, store and category')
    else:
        max_index = len(args) - 1
        print(max_index)
        for column in column_list:
            if index <= max_index:
                column['value'] = args[index]
            else:
                break
            index += 1

    return {"columns": [column_list]}


file = r'items\items_db_add_row.json'

keyspace = 'restapi'
table = 'items'

try:
    with open(file) as file:
        data = json.load(file)
except (FileNotFoundError| FileExistsError) as e:
    data = None

if data:
    body = format_and_change_values(data, 'Store2', 'Meat', 'uuid4', 'beef', 20.0)

    print(body)

    response = requests.post(
        f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v1/keyspaces/{keyspace}/tables/{table}/rows',
        headers=admin_headers,
        json=data
    )

    print(response.content)
    print(response.status_code)
