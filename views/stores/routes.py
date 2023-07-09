from flask import Blueprint
from flask_jwt_extended import jwt_required


stores_blueprint = Blueprint('stores', __name__)


@stores_blueprint.route('/store', methods=['POST', 'GET'])
@jwt_required()
def get_store():
    return {'State': 'Work in progress'}


@stores_blueprint.route('/stores', methods=['POST', 'GET'])
@jwt_required()
def get_stores():
    return {'State': 'Work in progress'}