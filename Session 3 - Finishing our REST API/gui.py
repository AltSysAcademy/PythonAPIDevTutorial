import requests as r

# Equivalent of POSTMAN in Python
url = "http://127.0.0.1:5000"
store_endpoint = f"{url}/store"
item_endpoint = f"{url}/item"

print("Main Menu:")
print("---------------------------")
print("Store Related Operations")
print("---------------------------")
print("1. Get all stores")
print("2. Get specific store by ID")
print("3. Create store")
print("4. Delete store by ID") # Assignment
print()
print("---------------------------")
print("Item Related Operations")
print("---------------------------")
print("5. Get all items") # Assignment
print("6. Get specific item by ID") # Assignment
print("7. Create store") # Assignment
print("8. Delete item by ID") # Assignment
print("9. Update item by ID") # Assignment
print("---------------------------")
print("0. Exit")
print()


# r.get, r.put, r.post, r.delete
while True:
    user_choice = input(">>> ")

    if user_choice == "1":
        # GET Request to our server and return it as a dictionary
        stores = r.get(store_endpoint).json()
        
        for store in stores:
            print("-------------------------")
            print(store["id"])
            print(store["name"])
            print("-------------------------")
            print()

    elif user_choice == "2":
        store_id = input("Enter store ID: ")
        store = r.get(f"{store_endpoint}/{store_id}").json()
        print(f"Store Found: {store['name']}")
    elif user_choice == "3":
        store_name = input("Enter store name: ")
        
        new_store = {"name": store_name}

        response = r.post(store_endpoint, json=new_store)

        if response.status_code == 201:
            print("Store has been added.")
        else:
            json = response.json()
            print(json["message"])



