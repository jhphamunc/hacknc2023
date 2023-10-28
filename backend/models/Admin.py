from User import User

class Admin(User):
    def __init__(self, f_name, l_name, phone_number, email, organization):
        super().__init__(self, f_name, l_name, phone_number, email, organization)
        self.organization = organization

    def get_name(self):
        return self.f_name + ' ' + self.l_name
    
    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email 
    
    def get_organization(self):
        return self.organization

    def set_f_name(self, f_name):
        self.f_name = f_name

    def set_l_name(self, l_name):
        self.l_name = l_name

    def set_email (self, email):
        self.email = email

    def set_organization (self, organization):
        self.organization = organization