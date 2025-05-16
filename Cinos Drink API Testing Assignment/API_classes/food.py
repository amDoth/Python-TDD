class Food:
    available_items = {"hotdog", "corndog", "ice cream", "onion rings", "french fries", "tater tots", "nacho chips"} #a list of food items offered by Cinos
    food_toppings = {"nacho cheese", "chili", "bacon bits", "ketchup", "mustard"} #a list of food toppings offered by Cinos
    ice_cream_toppings = {"cherry", "whipped cream", "caramel sauce", "chocolate sauce"} #a list of ice cream toppings offered by Cinos
    
    def __init__(self): #defines the initialization
        self._item = None
        self._toppings=[]
    
    def get_item(self): #gets the item of the Food object
        return self._item
    
    def get_toppings(self): #gets the list of toppings in the Food object
        toppings_list = []
        for topping in self._toppings:
            toppings_list.append(topping)
        return toppings_list
    
    def get_num_toppings(self): #gets the number of toppings in the Food object
        return len(self._toppings)
    
    def get_total(self): #calculates the total of the Food object it is used on
        item_cost = 0
        toppings_cost = 0
        #calculates the cost of the item
        if self._item == "hotdog": item_cost = 2.30
        elif self._item == "corndog": item_cost = 2.00
        elif self._item == "ice cream": item_cost = 3.00
        elif self._item == "onion rings": item_cost = 1.75
        elif self._item == "french fries": item_cost = 1.50
        elif self._item == "tater tots": item_cost = 1.70
        elif self._item == "nacho chips": item_cost = 1.90
        else: Exception("Error calculating total, invalid item")
        #calculates the cost of the toppings
        for topping in self._toppings:
            if topping == ("caramel sauce" or "chocolate sauce"):
                toppings_cost += 0.50
            elif topping == ("nacho cheese" or "bacon bits"):
                toppings_cost += 0.30
            elif topping == "chili":
                toppings_cost += 0.60
        #calculates the final cost
        return item_cost + toppings_cost
        
    
    def set_item(self, item): #sets the item of the Food object
        if item.lower() in Food.available_items:
            self._item = item
    
    def add_topping(self, topping): #adds a topping to the list of toppings in the Food object 
        if self._item == "ice cream":
            if topping.lower() in Food.ice_cream_toppings:
                self._toppings.append(topping)
            elif topping.lower() in Food.food_toppings:
                raise Exception("This topping is only available for food items.")
            else: raise Exception("ERROR")
        else:
            if topping.lower() in Food.ice_cream_toppings:
                raise Exception("This topping is only available for ice cream.")
            elif topping.lower() in Food.food_toppings:
                self._toppings.append(topping)
            else: raise Exception("ERROR")
    
    def set_toppings(self, toppings): #initialize with an array of toppings, sets the toppings of the Food object
        for topping in toppings:
            if topping.lower() in (Food.food_toppings or Food.ice_cream_toppings):
                self.add_topping(topping)
                
    def __str__(self): #defines the string that is passed as the description of the Food object
        item = self._item.title()
        toppings = ", ".join(self._toppings)
        total = self.get_total()
        if len(self._toppings) == 0:
            return f"{item} - {total}"
        else: 
            return f"{item} with {toppings} - {total}"