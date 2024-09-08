from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import StoreSchema

from models import StoreModel
from db import db
from sqlalchemy.exc import SQLAlchemyError

from flask_jwt_extended import jwt_required

# Creating a blueprint that would be later registered sa documentation
blp = Blueprint("stores", __name__, description="Operation on stores.")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    # Requires a fresh token
    @jwt_required(fresh=True)
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)

        db.session.delete(store)
        db.session.commit()

        return {"message": "Store deleted."}

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    # Data Validation with StoreSchema
    # Requires a fresh token
    @jwt_required()
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, new_store_data):
        store = StoreModel(**new_store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error has occured while creating a store.")
        
        return store, 201

