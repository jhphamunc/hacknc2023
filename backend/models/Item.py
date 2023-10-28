class Item ():
    def __init__(self, item_number, name, color, location):
        self.item_number = item_number 
        self.name = name
        self.color = color 
        self.location = location
    
    def get_item_number(self):
        return self.item_number

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_location(self):
        return self.location

    def set_item_number(self, item_number):
        self.item_number = item_number
    
    def set_name(self, name):
        self.name = name
    
    def set_color(self, color):
        self.color = color
    
    def set_location(self, location):
        self.location = location

_items = {}
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
        
add_item("Laptop", "Silver", "Office")
add_item("Phone", "Black", "Home")
add_item("Book", "Red", "Library")

print(_items)
remove_item()
print(_items)
result = find_item("Phone", None, None)
for item in result:
    print(item.get_name(), item.get_color(), item.get_location())
