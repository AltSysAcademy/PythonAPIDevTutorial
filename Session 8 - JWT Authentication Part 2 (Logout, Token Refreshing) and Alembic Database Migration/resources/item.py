import uuid

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ItemSchema, ItemUpdateSchema

from db import db
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError

from flask_jwt_extended import jwt_required

blp = Blueprint("items", __name__, description="Operations on items.")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    # Requires a fresh token
    @jwt_required(fresh=True)
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)

        # Delete an Item
        db.session.delete(item)
        db.session.commit()

        return {"message": "Item deleted."}

    # Idempotency - Sending multiple requests should only have the same result
    # Idempotency - When updating a nonexisting item, you should add it
    # Validates the update item
    # Requires a fresh token
    @jwt_required(fresh=True)
    @blp.arguments(ItemUpdateSchema) # JSON Payload/Body Request
    @blp.response(200, ItemUpdateSchema) # Returned Data by the API 
    def put(self, new_item_data, item_id):
        item = ItemModel.query.get(item_id)
    
        if item:
            item.name = new_item_data["name"]
            item.price = new_item_data["price"]
        else:
            # Create a new item
            item = ItemModel(**new_item_data)

        db.session.add(item)
        db.session.commit()
    
        return item


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        price = 2000

        return ItemModel.query.all()
    

    # Requires a fresh token
    @jwt_required()
    # Data Validation: JSON -> Blp.Arg -> POST Method
    @blp.arguments(ItemSchema) 
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        # ** kwargs - keyword arguments
        new_item = ItemModel(**item_data)

        try:
            # Add the new_item to the session
            db.session.add(new_item)
            # Save the changes
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error has occured while creating an item.")
        
        return new_item, 201