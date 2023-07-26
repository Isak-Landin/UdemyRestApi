import json


def create_template(username, email_address, password):
    template_file = 'users_db_current_structure.json'
    with open(template_file, 'r') as file:
        content = file.read()


def generate_user_id():
    pass


def generate_token_salt():
    pass


def created_at():
    pass


def create_role(role=0):
    pass


def format_and_change_values(original_json, username, email, password, user_id, token_salt, created_at_param, role):
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