from User import User

class Admin(User):
    def __init__(self, f_name, l_name, phone_number, email, username, password, location,):
        super().__init__(self, f_name, l_name, phone_number, email, username, password)
        self.location = location

    def get_full_name(self):
        return self.f_name + ' ' + self.l_name
    
    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email 
    
    def get_location(self):
        return self.location

    def get_password(self):
        return self.password

    def set_f_name(self, f_name):
        self.f_name = f_name

    def set_l_name(self, l_name):
        self.l_name = l_name

    def set_email (self, email):
        self.email = email

    def set_location (self, location):
        self.location = location

    def set_password(self, password):
        self.password = password

