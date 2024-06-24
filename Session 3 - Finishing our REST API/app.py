from flask import Flask, request
from db import items, stores
import uuid

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return list(stores.values())

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex

    if "name" in store_data:
        # Avoid store with same name
        for store in stores.values():
            if store_data["name"] == store["name"]:
                return {"message": "Store already exists."}, 400

        new_store = {
            "id": store_id,
            "name": store_data["name"]
        }

        stores.update(
            {store_id: new_store}
        )

        return new_store, 201 

@app.get('/store/<string:store_id>')
def get_store(store_id):
    if store_id in stores:
        return stores[store_id]
    
    return {"message": "Store not found."}, 404

# Create an endpoint to delete a store
@app.delete('/store/<string:store_id>')
def delete_store(store_id):
    if store_id in stores:
        del stores[store_id]
        return {"message": "Store Deleted."}
    else:
        return {"message": "Store not found."}, 404

##############

@app.post('/item')
def create_item():
    item_data = request.get_json()

    if "name" in item_data and "price" in item_data and "store_id" in item_data:
        for item in items.values():
            if item["name"] == item_data["name"]:
                return {"message": "Item name already exists."}, 400
            
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

    return {"message": "Item not found."}


# Create endpoint for deleting an Item
@app.delete('/item/<string:item_id>')
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted."}
    else:
        return {"message": "Item not found."}, 404

# Create an endpoint for updating an item
@app.put('/item/<string:item_id>')
def update_item(item_id):
    # The data from postman that we will use to update our item
    new_item_data = request.get_json()
    
    if "name" in new_item_data or "price" in new_item_data:
        # Check if the item exists
        if item_id in items:
            # Get the item
            item = items[item_id]

            # Update the item
            item |= new_item_data

            # Return the item
            return item
    
    return {"message": "Item not found."}, 404


if __name__ == '__main__':
    app.run()



# @app.post('/items')
# def multi_entry_items():
#     items_data = request.get_json() #List
#     new_items = []

#     for item_data in items_data:
#         if "name" in item_data and "price" in item_data and "store_id" in item_data:
#             for item in items.values():
#                 if item["name"] == item_data["name"]:
#                     return {"message": f"Item name already exists: {item["name"]}"}, 400
                
#             if item_data["store_id"] in stores:
#                 item_id = uuid.uuid4().hex

#                 new_item = {
#                     "id": item_id,
#                     "name": item_data["name"],
#                     "price": item_data["price"],
#                     "store_id": item_data["store_id"],
#                 }

#                 items.update({item_id:new_item})
#                 new_items.append(new_item)

#     return new_items, 201