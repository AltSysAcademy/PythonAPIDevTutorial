from flask import Flask, request
from db import items, stores
import uuid

# Responsible for the API Documentation
from flask_smorest import Api

# Import those two blueprints
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

# Create a flask web app
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

# Register the blueprints to API Documentation
api = Api(app) 
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

if __name__ == '__main__':
    app.run()
