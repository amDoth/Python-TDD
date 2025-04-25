class Drink:
    available_bases = {"water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"}
    available_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}
    
    def __init__(self):
        self._base = None
        self._flavors=[]
    
    def get_base(self):
        return self._base
    
    def get_flavors(self):
        flavors_list = []
        for flavor in self._flavors:
            flavors_list.append(flavor)
        return flavors_list
    
    def get_num_flavors(self):
        return len(self._flavors)
    
    def set_base(self, base):
        if base in Drink.available_bases:
            self._base = base
    
    def add_flavor(self, flavor):
        self._flavors.append(flavor)
    
    def set_flavors(self, flavors): #initialize with an array of flavors
        for flavor in flavors:
            self.add_flavor(flavor)
            
    def __str__(self):
        base = self._base 
        flavors = ", ".join(self._flavors)
        return f"{base} with {flavors}"

class Order:    
    
    def __init__(self):
        self._items = []
    
    def get_items(self):
        return self._items.copy()
    
    def get_num_items(self):
        return len(self._items)
    
    def get_total(self):
        return 3.00 * len(self._items) #assuming each drink is exactly $3.00
        
    def get_receipt(self):
        receipt_lines = ["Cinos Sales Receipt"]
        for drink in self._items:
            receipt_lines.append(str(drink))
        subtotal = self.get_total()
        tax = round(subtotal * 0.065, 2)
        total = round(subtotal + tax, 2)
        receipt_lines.append(f"Subtotal: ${subtotal:.2f}") 
        receipt_lines.append(f"Tax: ${tax:.2f}")
        receipt_lines.append(f"Total: ${total:.2f}")
        return "\n".join(receipt_lines)
        
    def add_item(self, drink):
        self._items.append(drink)
    
    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]