class User:
    def __init__(self, f_name, l_name, phone_number, email, username, password):
        self.f_name = f_name
        self.l_name = l_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    def full_name(self):
        return self.f_name + ' ' + self.l_name
    
    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email 
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def set_f_name(self, f_name):
        self.f_name = f_name

    def set_l_name(self, l_name):
        self.l_name = l_name

    def set_email (self, email):
        self.email = email
    
    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

users = []

def create_user():
    print("Create a new user:")
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    username = input ("Enter a username: ")
    password = input("Enter a password: ")

    new_user = User(f_name, l_name, phone_number, email, username, password)
    users.append(new_user)
    print("New user created!")

def login():
    print("User Login:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user.username == username and user.password == password:
            print("Login in successful!")
            print(f"Welcome, {user.full_name()} ")
            return
        print("Invlaid username and/or passowrd. Login Failed.")

while True:
    print("\n1. Create User \n2. Login \n3. Exit")
    choice = input("Enter your choice: ")

    if choice  == "1":
        create_user()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting program")
        break
    else:
        print("Invalid input.")

