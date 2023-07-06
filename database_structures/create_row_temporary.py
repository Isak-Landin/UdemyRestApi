import bcrypt
import requests
import json
from database_modules.localconfig import astra_id, admin_headers


def format_and_change_values(original_json, *args):
    # sourcery skip: simplify-len-comparison
    column_list = original_json['columns']
    index = 0
    if len(args) == len(column_list):
        for column in column_list:
            column['value'] = args[index]
            index += 1
    elif len(args) < 1:
        raise ValueError('Expected to get at least 1 argument, store')
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


file = r'users/users_db_add_row.json'

keyspace = 'restapi'
table = 'users'

try:
    with open(file) as file:
        data = json.load(file)
except (FileNotFoundError, FileExistsError) as e:
    data = None

if data:
    for i in range(10, 50):

        password = bcrypt.hashpw(f'password{i}'.encode(), salt=bcrypt.gensalt())
        print(password.decode())
        print(type(password))
        body = format_and_change_values(data, f'user{i}', f'email{i}@gmail.com', password.decode(), f'{i}', 0)

        print(body)

        response = requests.post(
            f'https://{astra_id}-europe-west1.apps.astra.datastax.com/api/rest/v1/keyspaces/{keyspace}/tables/{table}/rows',
            headers=admin_headers,
            json=data
        )

        print(response.content)
        print(response.status_code)