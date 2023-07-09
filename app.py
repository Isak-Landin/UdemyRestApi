from datetime import timedelta

from App_Config.app_config import jwt_secret
from server_stability import ServerStatus

from flask import Flask, abort
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

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



