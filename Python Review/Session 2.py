# Functions
# A command - utos sa machine
# Creation of commands, user-defined functions

# Define
# def introduce():
#     print("I am Altis Jessie Nino Dulay")

# # Calling a function
# introduce()

# Arguments, Paramaters (temporary variables)
# def add(x, y):
#     print(x + y)

# add(10,20)

# Return Statement
# Allows us to return a data
# Return statements allows us to save data in a variable to be used later
# def add(x, y):
#     print("We are adding two numbers...")
#     return x + y

# answer = add("Hello", 0.5)
# print(answer)


########
# While Loop
# Boolean-Based (Conditions)

# 0, 1, 2, 3, 4


# a = 0
# while a < 5: 
#     print(a) 
#     a += 1

# Break Statement - Breaks/stops the loop
# a = 0
# while a < 10: 
#     print(a) 
#     if a == 3:
#         break
#     a += 1


# Continue Statement - Skip an iteration
# a = 0
# while a < 10: 
#     a += 1
#     if a == 5:
#         continue
#     print(a)

# while True:
#     num1 = input("Enter first number: ")
#     if num1 == "Exit":
#         break

#     num2 = input("Enter second number: ")
#     answer = float(num1) + float(num2)

#     print(answer)


# For Loop
# Sequence/Iterable Based
# String, List, Dictionary

# Key-Value Pairs 


# profile1 = {
#     "name": "Altis",
#     "age": 20,
#     "contacts": [
#         {
#             "name": "Nino",
#             "age": 19
#         }, 
#         {
#             "name": "John",
#             "age": 21
#         }, 
#         {
#             "name": "Jane",
#             "age": 22
#         }, 
#         {
#             "name": "Joe",
#             "age": 23
#         }
#     ]
# }

# for contact in profile1["contacts"]:
#     if contact["name"] == "Jane":
#         break
#     print(contact)


# for key in profile1:
#     print(key)

# for value in profile1.values():
#     print(value)

# for contact in profile1["contacts"]:
#     print(contact)

# for contact in profile1["contacts"]:
#     for value in contact.values():
#         print(value)


# Object Oriented Programming
# Class - Blueprint of an Object
# Instance - The Object itself

# Blueprint of the Human Object
class Human:
    # Constructor - It runs when we create an instance of this class
    def __init__(self, name, age, address):
        # Attributes - Name, Age, Address
        self.name = name
        self.age = age
        self.address = address
    
    # Method - self is also a default parameter
    def introduce(self):
        print(f"I am {self.name}!")

    def walk(self):
        print("Walking....")
    
    def change_address(self, new_address):
        self.address = new_address
    
    def birthday(self, year):
        self.age += year
        
# Instantiation - Created an Object
person1 = Human("Altis Dulay", 20, "Meyc, Bulacan")

person1.introduce()
person1.walk()
person1.change_address("City of Meyc, Bulacan")
person1.birthday(2)

print(person1.age)