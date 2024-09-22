from db import stores
import uuid

# Get the JSON Payload from the postman
from flask import request

# MethodView - Group related API Methods 
from flask.views import MethodView

# Blueprint - Responsible for handling our routes and to create our API Documentation 
# abort - Used for returning error messages
from flask_smorest import Blueprint, abort


from schemas import StoreSchema

# Creating a blueprint that would be later registered sa documentation
# Blueprint(name, import_name, description), name and description would be displayed on the API Documentation
blp = Blueprint("Stores Endpoints", __name__, description="Operation on stores.")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        if store_id in stores:
            return stores[store_id]
        
        abort(404, message="Store not found.")

    def delete(self, store_id):
        if store_id in stores:
            del stores[store_id]
            return {"message": "Store Deleted."}
        else:
            abort(404, message="Store not found.")

@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return list(stores.values())

    def post(self, store_data):
        store_id = uuid.uuid4().hex

        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="Store already exists.")

        new_store = {
            "id": store_id,
            "name": store_data["name"]
        }

        stores.update(
            {store_id: new_store}
        )

        return new_store, 201 

