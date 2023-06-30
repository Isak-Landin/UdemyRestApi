from datetime import timedelta

import contextlib

from database_modules.get_items_api_connect import get_items as get_items_func
from App_Config.app_config import jwt_secret
from server_stability import ServerStatus

from flask import Flask, jsonify, request, abort

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
    client_request = request
    client_headers = client_request.headers

    try:
        with contextlib.suppress(AttributeError):
            client_data = client_request.json

    except AttributeError:
        client_data = None

    def login_with_cookies(_username, _password, header, json=None):
        return True

    def login_without_cookies(_username, _password, header, json=None):
        def is_valid_credentials(__username, __password):
            return True

        # Create logic that fits with JWTManager and Session
        if is_valid_credentials(__username=_username, __password=_password):
            access_token = create_access_token(identity=_username)
        else:
            access_token = None

        return access_token

    client_request = request.json

    username = client_request.get('username')
    password = client_request.get('password')

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
