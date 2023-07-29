from datetime import timedelta


from server_stability import ServerStatus

from flask import Flask, abort, jsonify
from JWTManagement.customized_jwt_manager import CustomJWTManager

from views.auth.routes import auth_blueprint as auth_bp
from views.items.routes import items_blueprint as items_bp
from views.stores.routes import stores_blueprint as stores_bp


def create_app():
    _app = Flask(__name__)
    _app.register_blueprint(auth_bp)
    _app.register_blueprint(items_bp)
    _app.register_blueprint(stores_bp)
    return _app


app = create_app()

@app.errorhandler(Exception)
def handle_exception(e):
    # create a response object
    response = {
        'error-message': 'There was a server error that prevented your request from executing as expected. The error has been logged and we are working on a fix this very moment.',
        'direct-error': str(e)
    }

    # convert the response to JSON format
    response = jsonify(response)

    # set the status code to 500 (Internal Server Error)
    response.status_code = 500

    # return the response
    return response


jwt_manager = CustomJWTManager(app)


@app.before_request
def is_server_stable():
    if not ServerStatus.is_server_stable():
        abort(500)



