from db import db

# Design a model for our store
class StoreModel(db.Model):
    __tablename__ = "stores"    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    # Define a relationship
    # One to Many - A Store Could Have More Than One Item
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")

    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic", cascade="all, delete")

'''

item = ItemModel.query.get(1)
store_1 = StoreModel.query.get(1)
store_2 = StoreModel.query.get(1)

store_1.items.remove(item)
store_2.items.append(item)

db.session.add(item)
db.session.add(store_1)
db.session.add(store_2)
db.session.commit()

print(store_1.items)

store_1 = {
    "id": 1,
    "name": "Bonay Store"
}
'''