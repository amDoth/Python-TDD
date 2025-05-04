class Drink:
    available_bases = {"water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"} #a list of bases for drinks offered by Cinos
    available_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"} #a list of flavors for drinks offered by Cinos
    sizes = {"small", "medium", "large", "mega"} #a list of sizes for drinks offered by Cinos
    
    def __init__(self, size): #defines the initialization
        self._base = None
        self._flavors=[]
        if size in Drink.sizes:
            self._size = size
        else: 
            raise Exception("Please enter a valid size (small, medium, large, or mega)")
    
    def get_base(self): #gets the base of the Drink object
        return self._base
    
    def get_flavors(self): #gets the list of flavors in the Drink object
        flavors_list = []
        for flavor in self._flavors:
            flavors_list.append(flavor)
        return flavors_list
    
    def get_size(self): #gets the size of the Drink object
        return self._size
    
    def get_num_flavors(self): #gets the number of flavors in the Drink object
        return len(self._flavors)
    
    def get_total(self): #calculates the total of the Drink object it is used on
        if self._size == "small":
            return 1.50 + len(self._flavors)*0.15 #calculation of a small drink
        elif self._size == "medium":
            return 1.75 + len(self._flavors)*0.15 #calculation of a medium drink
        elif self._size == "large":
            return 2.05 + len(self._flavors)*0.15 #calculation of a large drink
        elif self._size == "mega":
            return 2.15 + len(self._flavors)*0.15 #calculation of a mega drink
    
    def set_base(self, base): #sets the base of the Drink object
        if base in Drink.available_bases:
            self._base = base
    
    def add_flavor(self, flavor): #adds a flavor to the list of flavors in the Drink object 
        self._flavors.append(flavor)
    
    def set_flavors(self, flavors): #initialize with an array of flavors, sets the flavors of the Drink object
        for flavor in flavors:
            self.add_flavor(flavor)
    
    def set_size(self, size): #sets the size of the Drink object
        if size in Drink.sizes:
            self._size = size
        else:
            raise Exception("Please choose from small, medium, large, or mega")
            
    def __str__(self): #defines the string that is passed as the description of the Drink object
        base = self._base 
        flavors = ", ".join(self._flavors)
        size = self._size
        total = self.get_total()
        return f"{size} {base} with {flavors} - {total}"

class Order:    
    
    def __init__(self): #defines the initialization of the Order object, uses a list of Drink objects
        self._items = []
    
    def get_items(self): #gets the list of items in the Order object
        return self._items.copy()
    
    def get_num_items(self): #gets the number of items in the Order object
        return len(self._items)
    
    def get_total(self): #calculates the total of the Order object
        total = 0
        for drink in self._items:
            total += round(float(str(drink).split()[5]), 2) #for the total of the order, this line extracts the total 
        tax = round(total * 0.0725, 2)                      #from the __str__ method in the Drink object and makes it 
        return total + tax                                  #a float, then rounds it to two decimal places
        
    def get_receipt(self): #generates the receipt data, and includes \n for formatting purposes
        receipt_lines = ["Cinos Sales Receipt"]
        for drink in self._items:
            receipt_lines.append(str(drink))
        total = self.get_total()
        receipt_lines.append(f"Total including tax: ${total:.2f}")
        return "\n".join(receipt_lines)
        
    def add_item(self, drink): #adds a Drink object to the list of items in the Order object
        self._items.append(drink)
    
    def remove_item(self, index): #removes an item from the list of items in the Order object at the specified index
        if 0 <= index < len(self._items):
            del self._items[index]