from User import User

class Admin(User):
    def __init__(self, f_name, l_name, phone_number, email, username, password, organization, ):
        super().__init__(self, f_name, l_name, phone_number, email, username, password, organization)
        self.organization = organization

    def get_name(self):
        return self.f_name + ' ' + self.l_name
    
    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email 
    
    def get_organization(self):
        return self.organization

    def get_password(self):
        return self.password

    def set_f_name(self, f_name):
        self.f_name = f_name

    def set_l_name(self, l_name):
        self.l_name = l_name

    def set_email (self, email):
        self.email = email

    def set_organization (self, organization):
        self.organization = organization

    def set_password(self, password):
        self.password = password