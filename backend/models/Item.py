class Item ():
    def __init__(self, name, color, location):
        self.name = name
        self.color = color 
        self.location = location
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_location(self):
        return self.location

    def set_name(self, name):
        self._name = name
    
    def set_color(self, color):
        self.color = color
    
    def set_location(self, location):
        self.location = location

items = {}


    