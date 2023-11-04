#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items

# food menu
menu = {
    1: FoodItem(1, "Red bull", "250ml", 125, 5, 20),
    2: FoodItem(2, "Sambar Idly","1 plate", 150, 20, 3),
    3: FoodItem(3, "Mint Lime","1", 70, 20, 3),
    4: FoodItem(4, "Mayo corn sandwich","4 pieces", 80, 10, 40),
    5: FoodItem(5, "Double cheese Margherita","1", 180, 20, 3),
}

# User and admin
users = {}
admins = {"admin": "admin123"}  # Admin credentials (replace with a more secure mechanism)

# Order history 
order_history = []

# Admin functions
def add_food_item(name, quantity, price, discount, stock):
    food_id = max(menu.keys()) + 1
    menu[food_id] = FoodItem(food_id, name, quantity, price, discount, stock)

def edit_food_item(food_id, name, quantity, price, discount, stock):
    if food_id in menu:
        menu[food_id] = FoodItem(food_id, name, quantity, price, discount, stock)
    else:
        print("Food item not found.")

def view_food_items():
    for item_id, item in menu.items():
        print(f"Food ID: {item_id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}, Discount: {item.discount}%, Stock: {item.stock}")

def remove_food_item(food_id):
    if food_id in menu:
        del menu[food_id]
    else:
        print("Food item not found.")
        
def display_menu():
    print("Menu:")
    for item_id, item_info in menu.items():
        print(f"{item_id}. {item_info.name} ({item_info.quantity}) [INR {item_info.price:.2f}]")
# User functions
def register_user(full_name, phone_number, email, address, password):
    user = User(full_name, phone_number, email, address, password)
    users[email] = user

def login_user(email, password):
    if email in users and users[email].password == password:
        return users[email]
    return None

def place_order(user, items):
    order = Order(user, items)
    order_history.append(order)
    print("Order placed successfully!")

def display_order_history(user):
    print(f"Order history for {user.full_name}:")
    for order in order_history:
        if order.user == user:
            print(f"Items: {', '.join(item.name for item in order.items)}")

def update_user_profile(user, full_name, phone_number, email, address, password):
    user.full_name = full_name
    user.phone_number = phone_number
    user.email = email
    user.address = address
    user.password = password
    users[email] = user

# Main app
while True:
    print("\nWelcome to the Food Ordering App")
    print("1. Admin Login")
    print("2. User Registration")
    print("3. User Login")
    print("4. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        admin_email = input("Admin Email: ")
        admin_password = input("Admin Password: ")
        if admin_email in admins and admins[admin_email] == admin_password:
            while True:
                print("\nAdmin Menu")
                print("1. Add Food Item")
                print("2. Edit Food Item")
                print("3. View Food Items")
                print("4. Remove Food Item")
                print("5. Logout")
                admin_choice = input("Select an option: ")
                if admin_choice == "1":
                    name = input("Name: ")
                    quantity = input("Quantity: ")
                    price = float(input("Price: "))
                    discount = float(input("Discount (%): "))
                    stock = int(input("Stock: "))
                    add_food_item(name, quantity, price, discount, stock)
                elif admin_choice == "2":
                    food_id = int(input("Enter Food ID to edit: "))
                    name = input("Name: ")
                    quantity = input("Quantity: ")
                    price = float(input("Price: "))
                    discount = float(input("Discount (%): "))
                    stock = int(input("Stock: "))
                    edit_food_item(food_id, name, quantity, price, discount, stock)
                elif admin_choice == "3":
                    view_food_items()
                elif admin_choice == "4":
                    food_id = int(input("Enter Food ID to remove: "))
                    remove_food_item(food_id)
                elif admin_choice == "5":
                    print("Admin Logout")
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Invalid admin credentials.")

    elif choice == "2":
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        password = input("Password: ")
        register_user(full_name, phone_number, email, address, password)
        print("User registration successful.")

    elif choice == "3":
        user_email = input("User Email: ")
        user_password = input("User Password: ")
        user = login_user(user_email, user_password)
        if user:
            while True:
                print(f"\nWelcome!!, {user.full_name}")
                print("1. Place New Order")
                print("2. Order History")
                print("3. Update Profile")
                print("4. Logout")
                user_choice = input("Select an option: ")
                if user_choice == "1":
                    display_menu()
                    order_items = []
                    while True:
                        item_id = int(input("Enter the Food ID to add to the order (0 to finish): "))
                        if item_id == 0:
                            break
                        elif item_id in menu:
                            order_items.append(menu[item_id])
                        else:
                            print("Invalid Food ID.")
                    place_order(user, order_items)
                elif user_choice == "2":
                    display_order_history(user)
                elif user_choice == "3":
                    full_name = input("Full Name: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    address = input("Address: ")
                    password = input("Password: ")
                    update_user_profile(user, full_name, phone_number, email, address, password)
                    print("User profile updated.")


# In[ ]:




