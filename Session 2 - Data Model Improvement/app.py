from flask import Flask, request
from db import items, stores
import uuid

app = Flask(__name__)

## Improving our Data Model

# Updated so that it would use the new data model that we created
@app.get("/store")
def get_stores():
    return list(stores.values())

# Fix the code to use the new data model
@app.post("/store")
def create_store():
    store_data = request.get_json()

    # Create ID
    store_id = uuid.uuid4().hex

    new_store = {
        "id": store_id,
        "name": store_data["name"]
    }

    stores.update(
        {store_id: new_store}
    )

    # 201 - Creation successful
    return new_store, 201 

# Fixing the code
@app.get('/store/<string:store_id>')
def get_store(store_id):
    if store_id in stores:
        return stores[store_id]
    
    return {"message": "Store not found."}, 404

# Adjust code
@app.post('/item')
def create_item():
    item_data = request.get_json()

    if item_data["store_id"] in stores:
        item_id = uuid.uuid4().hex

        new_item = {
            "id": item_id,
            "name": item_data["name"],
            "price": item_data["price"],
            "store_id": item_data["store_id"],
        }

        items.update({item_id:new_item})

        return new_item, 201

    return {"message": "Store not found."}, 404

@app.get('/item')
def get_all_items():
    return list(items.values())

@app.get('/item/<string:item_id>')
def get_item(item_id):
    if item_id in items:
        return items[item_id]

    return {"message": "Item ID not found."}

if __name__ == '__main__':
    app.run(debug=True)