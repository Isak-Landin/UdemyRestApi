from datetime import timedelta

import contextlib

import flask

from database_modules.get_items_api_connect import get_items as get_items_func
from App_Config.app_config import jwt_secret
from server_stability import ServerStatus
from database_modules.validate_user import is_correct_password, is_user_exist_in_response, validate_user

from flask import Flask, jsonify, request, abort, Response

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = jwt_secret
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
app.config['JWT_SESSION_COOKIE'] = True

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)  # Set the access token expiration to 15 minutes
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # Set the refresh token expiration to 30 days

jwt = JWTManager(app)


@app.before_request
def is_server_stable():
    if not ServerStatus.is_server_stable():
        abort(500)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return abort(401)
    request_content_as_json: dict = request.get_json()
    request_headers_as_dict = dict(request.headers)
    content_type = request_headers_as_dict.get('Content-Type')

    response = flask.Response()

    def login_with_cookies(_username, _password, headers, json=None):
        return False

    def login_without_cookies(_username, _password, headers=None, json=None):
        is_valid_user = validate_user(username=str(_username), password=str(_password))

        print('User validity: ', is_valid_user)

        # Create logic that fits with JWTManager and Session
        if is_valid_user:
            access_token = create_access_token(identity=_username)
        else:
            access_token = None

        return access_token

    username = request_content_as_json.get('username')
    password = request_content_as_json.get('password')
    print(username, password)
    access = request_headers_as_dict.get('Authorization')

    if username and password:
        print('Username and password exists')
        access_token = login_without_cookies(_username=username, _password=password)
        print('My access-token', access_token)
        if access_token:
            response = jsonify(access_token=access_token)
            response.status_code = 200
            response.headers['Content-Type'] = 'application/json'
            response.headers['Custom-Header'] = 'Some value'

            return response
    elif access:
        login_with_cookies()
    else:
        return jsonify({'msg': 'Invalid or no credentials'})

    return jsonify(message='Invalid credentials'), 401


@app.route('/item', methods=['POST', 'GET'])
@jwt_required()
def get_item():
    return {'State': 'Work in progress'}


@app.route('/items', methods=['POST', 'GET'])
@jwt_required()
def get_items():
    return get_items_func()


@app.route('/store', methods=['POST', 'GET'])
@jwt_required()
def get_store():
    return {'State': 'Work in progress'}


@app.route('/stores', methods=['POST', 'GET'])
@jwt_required()
def get_stores():
    return {'State': 'Work in progress'}
