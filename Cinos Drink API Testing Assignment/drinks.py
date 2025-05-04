class Drink:
    available_bases = {"water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"}
    available_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}
    sizes = {"small", "medium", "large", "mega"}
    
    def __init__(self, size):
        self._base = None
        self._flavors=[]
        if size in Drink.sizes:
            self._size = size
        else: 
            raise Exception("Please enter a valid size (small, medium, large, or mega)")
    
    def get_base(self):
        return self._base
    
    def get_flavors(self):
        flavors_list = []
        for flavor in self._flavors:
            flavors_list.append(flavor)
        return flavors_list
    
    def get_size(self):
        return self._size
    
    def get_num_flavors(self):
        return len(self._flavors)
    
    def get_total(self):
        if self._size == "small":
            return 1.50 + len(self._flavors)*0.15
        elif self._size == "medium":
            return 1.75 + len(self._flavors)*0.15
        elif self._size == "large":
            return 2.05 + len(self._flavors)*0.15
        elif self._size == "mega":
            return 2.15 + len(self._flavors)*0.15
    
    def set_base(self, base):
        if base in Drink.available_bases:
            self._base = base
    
    def add_flavor(self, flavor):
        self._flavors.append(flavor)
    
    def set_flavors(self, flavors): #initialize with an array of flavors
        for flavor in flavors:
            self.add_flavor(flavor)
    
    def set_size(self, size):
        if size in Drink.sizes:
            self._size = size
        else:
            raise Exception("Please choose from small, medium, large, or mega")
            
    def __str__(self):
        base = self._base 
        flavors = ", ".join(self._flavors)
        size = self._size
        total = self.get_total()
        return f"{size} {base} with {flavors} - {total}"

class Order:    
    
    def __init__(self):
        self._items = []
    
    def get_items(self):
        return self._items.copy()
    
    def get_num_items(self):
        return len(self._items)
    
    def get_total(self):
        total = 0
        for drink in self._items:
            total += round(float(str(drink).split()[5]), 2)
        tax = round(total * 0.0725, 2)
        return total + tax
        
    def get_receipt(self):
        receipt_lines = ["Cinos Sales Receipt"]
        for drink in self._items:
            receipt_lines.append(str(drink))
        total = self.get_total()
        receipt_lines.append(f"Total including tax: ${total:.2f}")
        return "\n".join(receipt_lines)
        
    def add_item(self, drink):
        self._items.append(drink)
    
    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]