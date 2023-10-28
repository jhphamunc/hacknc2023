from models.user import User
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
    
    def login(username, password):
        print("User Login:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        for user in _users:
            if user.username == username and user.password == password:
                print("Login in successful!")
                print(f"Welcome, {user.get_full_name()}")
                return
        print("Invlaid username and/or passowrd. Login Failed.")


    item_number = 0

    def add_item(name, color, location):
        global item_number 
        _items[item_number] = {'name': name, 'color': color, 'location': location}
        item_number += 1

    def remove_item(item_number):
        del _items[item_number]
    
    # inputname = input[0]
    # inputc = input[1]
    # input location = input[2]

    # find_item()
    
    def find_item(name, color, location):
        input_name = True
        input_color = True 
        input_location = True
        
        if name == None: 
            input_name = False 
        
        if color == None: 
            input_color = False 

        if location == None: 
            input_location = False 
            
        if not(input_name & input_color & input_location):
            print("Please input a filter")
        
        
        #else:
        