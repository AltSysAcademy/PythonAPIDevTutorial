from db import db

class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    # Relationship between tag and store
    store = db.relationship("StoreModel", back_populates="tags")


    # Define a many-many relationship with items
    items = db.relationship("ItemModel", back_populates="tags", secondary="item_tags")

# tag = TagModel.query.get(1)
# return tag.items.all()