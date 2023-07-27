import json
import time
import uuid
from pathlib import Path

from database_modules.users_table.update_user_salt import update_salt

from GeneralUtils.decorators import standard_procedure

from JWTManagement.TokenGeneration import Tokens


@standard_procedure
def create_template(username, email_address, password):
    where_am_i = str(Path().resolve())
    template_file = f'{where_am_i}/database_structures/users/users_db_add_row.json'
    with open(template_file, 'r') as file:
        content = file.read()

    # Todo Dont forget to hash the password first, think through it.
    return format_and_change_values(content, username, email_address, password, generate_user_id(username), create_new_salt(), created_at(), create_role())




@standard_procedure
def generate_user_id(username):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, username))

@standard_procedure
def create_new_salt():
    return str(Tokens.create_new_token_salt())

@standard_procedure
def created_at():
    return int(time.time())

@standard_procedure
def create_role(role=0):
    return role

@standard_procedure
def format_and_change_values(original_json, username, email, password, user_id, token_salt, created_at_param, role) -> dict:
    original_json = json.loads(original_json)
    column_list = original_json['columns']
    for column in column_list:
        match column['name']:
            case 'username':
                column['value'] = username
            case 'email-address':
                column['value'] = email
            case 'password':
                column['value'] = password
            case 'user-id':
                column['value'] = user_id
            case 'token-salt':
                column['value'] = token_salt
            case 'created-at':
                column['value'] = created_at_param
            case 'role':
                column['value'] = role

        print(column)

    return original_json