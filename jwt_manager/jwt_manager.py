from flask_jwt_extended import JWTManager


class CustomJWTManager(JWTManager):
    def __init__(self, app=None):
        super().__init__(app)

    def _get_default_user_loader_callback(self):
        # Implement your own logic for loading the user from your storage system
        # Return the loaded user object or None if not found
        # Example:
        def load_user(identity):
            # Your code to load the user based on the identity (e.g., user ID)
            # Returns the loaded user object or None if not found
            pass

        return load_user

    def _get_default_blacklist_checker_callback(self):
        # Implement your own logic for checking if a token is blocklisted
        # Return True if the token is blocklisted, False otherwise
        # Example:
        def is_token_blacklisted(decoded_token):
            # Your code to check if the token is blocklisted
            # Return True if blocklisted, False otherwise
            pass

        return is_token_blacklisted