from flask import Blueprint, jsonify, request, abort, Response
from flask_jwt_extended import jwt_required

from JWTManagement.TokenGeneration import Tokens

auth_blueprint = Blueprint('auth', __name__)


def login_with_tokens(_username, _password, access_token, refresh_token):
    # Future code here
    return False


def login_without_tokens(_username, _password):
    if tokens := Tokens.generate_token_pair(
        username=str(_username), password=str(_password)
    ):
        __access_token, __refresh_token = tokens
    else:
        __access_token = None
        __refresh_token = None

    return __access_token, __refresh_token


@auth_blueprint.route('/login', methods=['POST'])
def login():
    if request.method == 'GET':
        return abort(401)

    request_content_as_json: dict = request.get_json()
    username = request_content_as_json.get('username')
    password = request_content_as_json.get('password')

    request_headers_as_dict = dict(request.headers)
    access_token = request_headers_as_dict.get('Authorization')
    refresh_token = request_headers_as_dict.get('Authorization-Refresh')
    content_type = request_headers_as_dict.get('Content-Type')  # for future use

    if username and password and not access_token and not refresh_token:
        access_token, refresh_token = login_without_tokens(_username=username, _password=password)
        if access_token and refresh_token:
            response = jsonify(access_token=access_token, refresh_token=refresh_token)
            response.status_code = 200
            response.headers['Content-Type'] = 'application/json'
            return response
    elif access_token and refresh_token:
        login_with_tokens(username, password, access_token, refresh_token)
    else:
        return jsonify({'msg': 'Invalid or no credentials'}), 401


@auth_blueprint.route('/refresh', methods=['POST', 'GET'])
@jwt_required(refresh=True)
def refresh():
    # Future code here
    return {}