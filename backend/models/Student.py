from User import User

class Student(User):
    def __init__(self, f_name, l_name, phone_number, email, username, password, pid):
        super().__init__(self, f_name, l_name, phone_number, username, password, email)
        self.pid = pid

    def get_full_name(self):
        return self.f_name + ' ' + self.l_name
    
    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email 
    
    def get_pid(self):
        return self.pid
    
    def get_password(self):
        return self.password

    def set_f_name(self, f_name):
        self.f_name = f_name

    def set_l_name(self, l_name):
        self.l_name = l_name

    def set_email (self, email):
        self.email = email
    
    def set_pid (self, pid):
        self.pid = pid 

    def set_password(self, password):
        self.password = password
    
