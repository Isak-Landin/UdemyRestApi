from flask_jwt_extended import create_access_token, create_refresh_token
from typing import Tuple


class Tokens:
    @staticmethod
    def generate_token_pair(username) -> Tuple[str, str]: