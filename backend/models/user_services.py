from user import User
from item import Item

_users = {}
_items = {}

class User_Services:

    def reset(self):
        global _users, _items
        _users = {}
        _items = {}

    def create_user():
        print("Create a new user:")
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        username = input ("Enter a username: ")
        password = input("Enter a password: ")

        new_user = User(f_name, l_name, phone_number, email, username, password)
        _users.append(new_user)
        print("New user created!")

    def login():
        print("User Login:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for user in _users:
            if user.username == username and user.password == password:
                print("Login in successful!")
                print(f"Welcome, {user.get_full_name()} ")
                return
            print("Invlaid username and/or passowrd. Login Failed.")

    item_number = 0

    def add_item(name, color, location):
        global item_number 
        _items[item_number] = {'name': name, 'color': color, 'location': location}
        item_number += 1

    def remove_item(item_number):
        del _items[item_number]

    def find_item(name=None, color=None, location=None):
        matching_items = []
        for item_number, item_info in _items.items():
            if (name is None or item_info['name'] == name) and \
            (color is None or item_info['color'] == color) and \
            (location is None or item_info['location'] == location):
                matching_items.append(Item(item_number, item_info['name'], item_info['color'], item_info['location']))
        return matching_items
        