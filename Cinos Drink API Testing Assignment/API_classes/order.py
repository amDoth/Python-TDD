from .drinks import Drink
from .food import Food
from .ice_storm import Ice_Storm
class Order:    
    
    def __init__(self): #defines the initialization of the Order object, uses a list of Drink/Food objects
        self._items = []
    
    def get_items(self): #gets the list of items in the Order object
        return self._items.copy()
    
    def get_num_items(self): #gets the number of items in the Order object
        return len(self._items)
    
    def get_total(self): #calculates the total of the Order object
        total = 0
        for item in self._items:
            if isinstance(item, Drink): #checks if the current item is a Drink object
                total += Drink.get_total(item) #uses the Drink get_total method with the item
            elif isinstance(item, Food): #checks if the current item is a Food object
                total += Food.get_total(item) #uses the Food get_total method with the item
            elif isinstance(item, Ice_Storm): #checks if the current item is an Ice_Storm object
                total += Ice_Storm.get_total(item) #uses the Ice_Storm get_total method with the item
        tax = round(total * 0.0725, 2)
        return total + tax
        
    def get_receipt(self): #generates the receipt data, and includes \n for formatting purposes
        receipt_lines = ["Cinos Sales Receipt"]
        for drink in self._items:
            receipt_lines.append(str(drink))
        total = self.get_total()
        receipt_lines.append(f"Total including tax: ${total:.2f}")
        return "\n".join(receipt_lines)
        
    def add_item(self, item): #adds a Drink object to the list of items in the Order object
        self._items.append(item)
    
    def remove_item(self, index): #removes an item from the list of items in the Order object at the specified index
        if 0 <= index < len(self._items):
            del self._items[index]