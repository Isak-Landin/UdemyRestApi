from flask import Blueprint, jsonify, request, abort, Response
from flask_jwt_extended import create_refresh_token, create_access_token
from flask_jwt_extended import jwt_required


register_blueprint = Blueprint('register', __name__)


@register_blueprint.route('register', methods=['POST'])
def register():
    # TODO
    #  Validate the legitimacy of the client-request.
    #  Validate that email and username is not already registered
    #  Add the user to all relevant dbs, this includes but is not limited to; UserTokens, users
    pass