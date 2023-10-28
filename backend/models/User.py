class User:
    def __init__(self, f_name, l_name, phone_number, email, username, password):
        self.f_name = f_name
        self.l_name = l_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    def get_full_name(self):
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
    

#while True:
    #print("\n1. Create User \n2. Login \n3. Exit")
    #choice = input("Enter your choice: ")

    #if choice  == "1":
        #sign_up()
    #elif choice == "2":
        #login()
    #elif choice == "3":
        #print("Exiting program")
        #break
    #else:
        #print("Invalid input.")