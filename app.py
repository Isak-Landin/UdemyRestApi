from datetime import timedelta

from flask import Flask, jsonify, request
from database_modules.get_items import get_items as get_items_func
from flask_jwt_extended import jwt_required, JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'test'
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
app.config['JWT_SESSION_COOKIE'] = True

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)  # Set the access token expiration to 15 minutes
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # Set the refresh token expiration to 30 days
jwt = JWTManager(app)


@app.route('/login', methods=['POST', 'GET'])
def login():

    def is_valid(_username, _password):
        return False

    client_request = request.json

    username = client_request.get('username')
    password = client_request.get('password')

    if is_valid(_username=username, _password=password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

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
