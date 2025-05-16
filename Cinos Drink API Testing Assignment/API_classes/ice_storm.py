from enum import Enum

class Ice_Storm_Toppings_Prices(Enum):
    cherry = 0.00
    whipped_cream = 0.00
    caramel_sauce = 0.50
    chocolate_sauce = 0.50
    storios = 1.00
    dig_dogs = 1.00
    tnts = 1.00
    cookie_dough = 1.00
    pecans = 0.50
    
class Ice_Storm_Flavor_Prices(Enum):
    mint_chocolate_chip = 4.00
    chocolate = 3.00
    vanilla_bean = 3.00
    banana = 3.50
    butter_pecan = 3.50
    smore = 4.00

class Ice_Storm():
    def __init__(self): #defines the initialization
        self._flavor = None
        self._toppings=[]
    
    def get_flavor(self): #gets the flavor of the Ice_Storm object
        return self._flavor
    
    def get_toppings(self): #gets the list of toppings in the Ice_Storm object
        toppings_list = []
        for topping in self._toppings:
            toppings_list.append(topping)
        return toppings_list
    
    def get_num_toppings(self): #gets the number of toppings in the Ice_Storm object
        return len(self._toppings)
    
    def get_total(self): #calculates the total of the Ice_Storm object it is used on
        flavor = self._flavor
        total = Ice_Storm_Flavor_Prices[flavor].value
        for topping in self._toppings:
            total += Ice_Storm_Toppings_Prices[topping].value
        return total    
    
    def set_flavor(self, flavor): #sets the flavor of the Ice_Storm object
        if flavor.lower() in Ice_Storm_Flavor_Prices.__members__:
            self._flavor = flavor
        else: raise Exception("This flavor is not available")
    
    def add_topping(self, topping): #adds a topping to the list of toppings in the Ice_Storm object 
        if topping.lower() in Ice_Storm_Toppings_Prices.__members__:
            self._toppings.append(topping)
        else: raise Exception("This topping is not available")
    
    def set_toppings(self, toppings): #initialize with an array of toppings, sets the toppings of the Ice_Storm object
        for topping in toppings:
            if topping.lower() in Ice_Storm_Toppings_Prices.__members__:
                self.add_topping(topping)
    
    def remove_topping(self, index): #removes a topping from the list of toppings in the Ice_Storm object
        if 0 <= index < len(self._toppings):
            del self._toppings[index]
                
    def __str__(self): #defines the string that is passed as the description of the Food object
        flavor = self._flavor.replace("_", " ").title()
        toppings = ", ".join(self._toppings)
        total = self.get_total()
        if len(self._toppings) == 0:
            return f"{flavor} ice storm - {total:.2f}"
        else: 
            return f"{flavor} ice storm with {toppings} - {total:.2f}"