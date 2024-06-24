# Print Statements
# print("Hello")

# Comments
# Programmer's Notes/Annotation
# This is not executed by python

# Data Types
'''
String - Textual w "" | "Hello", "123"
Integer - Numerical Data w/o "" | 1, -5, 0
Float - Integer w/ Decimal Point | 1.1, -0.0, -1.1
Boolean - Boolean Value (True, False) 
'''

# Variables
string_var = "Nino"
int_var = 10
float_var = 1.5
bool_var = True

# Variable name should not have any special symbols or spaces
full_name = ""
school_address = ""

# print(bool_var)


# # String Interpolation
# name = "Nino"
# age = 20

# # My name is {Nino} and I am {20} years old
# # f""
# print(f"My name is {name} and I am {age} years old")



######
# Inputs
# A way for us to gather data from a user
# FORMAT: var = input(prompt)
# username = input("Enter username: ")
# print(f"The data you gave us: {username}")

# Add 2 numbers from user input
# num1 = input("Enter number: ")
# num2 = input("Enter another number: ")
# answer = float(num1) + float(num2)
# print(answer)

# Casting - Type Conversion
# old_data_type -> new_data_type
# FORMAT: new_type(old_data)
# a = "5"
# b = int(a)

# Mathematics
# print(1+1)
# print(1-1)
# print(1*1)
# print(1/1)

# Exponentation
# print(5**3) # 5*5*5

# Floor Division
# print(10//6)

# Modulo - Gets the remainder
# print(10%3) # 10 / 3 = 3 r1

# Booleans - True or False
# Logical Conditions
# Boolean Operators
'''
Comparison Operators:
>  - Greater than
<  - Less than
>= - Greater than or equal
<= - Less than or equal
== - Equal to
!= - Not Equal
'''
'''
Logical Operators:
and  - Kapag lahat ay true, true
or   - Kahit isa ay true, true
not  - Kapag true, false
'''
# print(10 != 50)

# print(not(True))

# If, Elif, Else
a = 10
b = 10

# If the condition became true- then the indented code would run
# if a > b:
#     print("Good Morning")
# elif a < b:
#     print("Good Evening")
# elif a < b:
#     print("Good Evening")
# elif a < b:
#     print("Good Evening")
# else:
#     print("Good afternoon")


# Lists
# Lists of data
nums = [10,20,30,40,50]

# # Indexing - Access a particular element
# # We start counting by 0 in programming
# #       0  1  2  3  4
# nums = [10,20,30,40,50]
# print(nums[1])

# Add an item in a list
# nums = [10,20,30,40,50]
# nums.append(60)
# print(nums)

# Insert an item
#       0  1  2  3  4  5
# nums = [10,20,30,40,50]
# nums.insert(2, "O")
# print(nums)

# Delete an item
# nums = [10,20,30,40,50]
# nums.pop(0)
# print(nums)

# Change/Update an item
# nums = [10, 20, 30]
# nums[1] = 50
# print(nums)


# Dictionary - like lists but instead of index, we use keys
profile = {
    "name": "Nino",
    "age": 20,
    "hobby": "Gaming"
}

# Print a specific key-value pair
# print(profile["hobby"])

# Adding a new item
# profile = {
#     "name": "Nino",
#     "age": 20,
#     "hobby": "Gaming"
# }
# profile.update({"salary": 10000})
# print(profile)

# Edit an item
# profile = {
#     "name": "Nino",
#     "age": 20,
#     "hobby": "Gaming"
# }

# dict2 = {
#     "name": "Altis",
#     "salary": 10000
# }

# profile |= dict2

# print(profile)

# Add key-value pair from another dictionary to dictionary
# profile = {
#     "name": "Nino",
#     "age": 20,
#     "hobby": "Gaming"
# }

# unused_dict = {**profile, "salary": 10000, "address": "Meycauayan, Bulacan"}
# print(unused_dict)

# profile.update({"name": "Altis"})
# print(profile)

# Deleting a key value pair
# profile = {
#     "name": "Nino",
#     "age": 20,
#     "hobby": "Gaming"
# }
# del profile["name"]

# print(profile)