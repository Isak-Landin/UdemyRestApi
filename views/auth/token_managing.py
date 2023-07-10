from datetime import timedelta

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager

import flask

from App_Config.app_config import jwt_secret


class TokenManager:
    def __init__(self, app_to_bind: flask.app.Flask):
        self.jwt_manager: JWTManager = None
        self.bound_app: flask.app.Flask = app_to_bind

        self.jwt_manager_configuration = \
            {
                'JWT_SECRET_KEY': jwt_secret,
                'JWT_TOKEN_LOCATION': ['headers', 'cookies'],
                'JWT_SESSION_COOKIE': True,
                'JWT_ACCESS_TOKEN_EXPIRES': timedelta(minutes=15),
                'JWT_REFRESH_TOKEN_EXPIRES': timedelta(days=30)
            }

        self.initialize_jwt_manager_on_startup()

    def bind_app_to_jwt_manager(self, app_to_bind: flask.app.Flask):
        self.jwt_manager.init_app(app_to_bind)

    def bind_jwt_manager_configurations_to_app(self):
        """
        app.config['JWT_SECRET_KEY'] = jwt_secret
        app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
        app.config['JWT_SESSION_COOKIE'] = True

        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)  # Set the access token expiration to 15 minutes
        app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
        # Set the refresh token expiration to 30 days
        """
        for key, value in self.jwt_manager_configuration.items():
            self.bound_app.config[key] = value

    def initialize_jwt_manager_on_startup(self):
        self.jwt_manager = JWTManager()

    @staticmethod
    def refresh_refresh_token(refresh_token):
        pass

