from flask import Flask, request, jsonify
from db import db
from flask_jwt_extended import JWTManager, create_refresh_token, get_jwt

from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint

import os

from blocklist import BLOCKLIST
from datetime import timedelta

from flask_migrate import Migrate

def create_app(db_url=None):
    app = Flask(__name__)

    # Setup the configs
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"

    # Responsible for the documentation website
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Setup what database we are going to use.
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    # Connect our flask_sqlalchemy to flask
    db.init_app(app)
    migrate = Migrate(app, db)

    # We need to create all the models that we have designed
    '''
    with app.app_context():
        db.create_all()
    '''
        
    # Register the blueprints to API Documentation
    api = Api(app) 
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    # SETUP A SECRET KEY FOR JWT
    app.config["JWT_SECRET_KEY"] = "221183046710680362485358125809847539027"
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
    # Create a JWT Manager Object
    jwt = JWTManager(app)


    # Add the custom error messages
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "message": "The token has expired.", 
                    "error": "token_expired"
                }
            ),
            401
        )
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {
                    "message": "Signature verification failed.", 
                    "error": "invalid_token"
                }
            ),
            401
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "message": "Request does not contain an access token.", 
                    "error": "authorization_required"
                }
            ),
            401
        )

    # Responsible for changing a JWT claim
    @jwt.additional_claims_loader
    def add_claim_to_jwt(identity):
        # user = UserModel.query.get(identity)
        # if user.is_admin == 1:
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}
    

    # Checks everytime if the JTI of the JWT is in the blocklist
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        # True or False
        return jwt_payload["jti"] in BLOCKLIST
    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
