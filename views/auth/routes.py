from flask import Blueprint, jsonify, request, abort, Response
from flask_jwt_extended import create_refresh_token, create_access_token
from flask_jwt_extended import jwt_required

from validate_user import validate_user_login


auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login', methods=['POST'])
def login():
    if request.method == 'GET':
        return abort(401)
    request_content_as_json: dict = request.get_json()
    request_headers_as_dict = dict(request.headers)
    content_type = request_headers_as_dict.get('Content-Type')

    response = Response()

    def login_with_cookies(_username, _password, headers, json=None):
        return False

    def login_without_cookies(_username, _password, headers=None, json=None):
        is_valid_user = validate_user_login(username=str(_username), password=str(_password))

        # Create logic that fits with JWTManager and Session
        if is_valid_user:
            __access_token = create_access_token(identity=_username)
            __refresh_token = create_refresh_token(identity=_username)
        else:
            __access_token = None
            __refresh_token = None

        return __access_token, __refresh_token

    username = request_content_as_json.get('username')
    password = request_content_as_json.get('password')
    access = request_headers_as_dict.get('Authorization')

    if username and password:
        access_token, refresh_token = login_without_cookies(_username=username, _password=password)
        if access_token and refresh_token:
            response = jsonify(access_token=access_token, refresh_token=refresh_token)
            response.status_code = 200
            response.headers['Content-Type'] = 'application/json'

            return response
    elif access:
        login_with_cookies()
    else:
        return jsonify({'msg': 'Invalid or no credentials'})

    return jsonify(message='Invalid credentials'), 401


@auth_blueprint.route('/refresh', methods=['POST', 'GET'])
@jwt_required(refresh=True)
def refresh():
    return {}