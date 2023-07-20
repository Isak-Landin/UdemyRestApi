from datetime import timedelta


from server_stability import ServerStatus

from flask import Flask, abort
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

jwt_manager = CustomJWTManager(app)


@app.before_request
def is_server_stable():
    if not ServerStatus.is_server_stable():
        abort(500)



