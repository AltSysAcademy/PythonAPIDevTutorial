from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(), nullable=True)
    price = db.Column(db.Float, unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),unique=False, nullable=False)
    store = db.relationship("StoreModel", back_populates="items")


    # Connect the ItemModel to have tags column
    tags = db.relationship("TagModel", back_populates="items",secondary="item_tags")


'''
item1 = ItemModel(name="Chair", price=120, store_id=1)

item1 = {
    "id": 1,
    "name": "Chair",
    "price": 120.00,
    "store_id": 1,
    "store": {
        "id": 1,
        "name": "Furniture Store"
    }
}
'''