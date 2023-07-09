from flask import Blueprint
from flask_jwt_extended import jwt_required

from database_modules.get_items_api_connect import get_items as get_items_func


items_blueprint = Blueprint('items', __name__)


@items_blueprint.route('/item', methods=['POST', 'GET'])
@jwt_required()
def get_item():
    return {'State': 'Work in progress'}


@items_blueprint.route('/items', methods=['POST', 'GET'])
@jwt_required()
def get_items():
    return get_items_func()
