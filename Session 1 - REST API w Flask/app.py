from flask import Flask, request

# Flask - is an object that allows us to run a local web server
# Create a Flask Web App
app = Flask(__name__)


# Structure of the Data
# Mock Database - Fake Database
stores = [
    {
        "id": 1,
        "name": "My Store 1", 
        "items": [
            {
                "name": "Chair",
                "price": 19.99
            }
        ]
    }
]

# Creating our very first endpoint
# '/store' endpoint
@app.get("/store")
def get_stores():
    return stores

# Creating our second endpoint
@app.post("/store")
def create_store():
    # Get the JSON Payload from the POST Request
    store_data = request.get_json()

    # Create a new store using dictionary
    new_store = {
        "name": store_data["name"],
        "items": []
    }

    stores.append(new_store)
    
    return new_store, 201

# Create a new endpoint where in we utilize URL Segments
# FORMAT: endpoint/<dtype: var_name>
@app.get('/store/<string:store_name>')
def get_store(store_name):
    for store in stores:
        if store["name"] == store_name:
            return store

# Create a new endpoint to create a new item
@app.post('/store/<string:store_name>/item')
def create_item(store_name):
    item_data = request.get_json()

    for store in stores:
        if store["name"] == store_name:
            new_item = {
                "name": item_data["name"],
                "price": item_data["price"]
            }

            store["items"].append(new_item)
            return new_item, 201
    
    return {"message": "Store not found."}, 404

# Get items from a store
@app.get('/store/<string:store_name>/item')
def get_items_from_store(store_name):
    for store in stores:
        if store["name"] == store_name:
            return store["items"]
        
    return {"message": "Store not found."}, 404

# This would run our flask web app
if __name__ == '__main__':
    app.run(debug=True)