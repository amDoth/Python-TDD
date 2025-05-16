class Drink:
    available_bases = {"water", "sbrite", "pokeacola", "mr. salt", "hill fog", "leaf wine"} #a list of bases for drinks offered by Cinos
    available_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"} #a list of flavors for drinks offered by Cinos
    sizes = {"small", "medium", "large", "mega"} #a list of sizes for drinks offered by Cinos
    
    def __init__(self, size): #defines the initialization
        self._base = None
        self._flavors=[]
        if size.lower() in Drink.sizes:
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
        if self._size.lower() == "small":
            return 1.50 + len(self._flavors)*0.15 #calculation of a small drink
        elif self._size.lower() == "medium":
            return 1.75 + len(self._flavors)*0.15 #calculation of a medium drink
        elif self._size.lower() == "large":
            return 2.05 + len(self._flavors)*0.15 #calculation of a large drink
        elif self._size.lower() == "mega":
            return 2.15 + len(self._flavors)*0.15 #calculation of a mega drink
    
    def set_base(self, base): #sets the base of the Drink object
        if base.lower() in Drink.available_bases:
            self._base = base
    
    def add_flavor(self, flavor): #adds a flavor to the list of flavors in the Drink object 
        if flavor.lower() in Drink.available_flavors: 
            self._flavors.append(flavor)
    
    def set_flavors(self, flavors): #initialize with an array of flavors, sets the flavors of the Drink object
        for flavor in flavors:
            if flavor.lower() in Drink.available_flavors:
                self.add_flavor(flavor)
    
    def set_size(self, size): #sets the size of the Drink object
        if size.lower() in Drink.sizes:
            self._size = size
        else:
            raise Exception("Please choose from small, medium, large, or mega")
            
    def __str__(self): #defines the string that is passed as the description of the Drink object
        base = self._base 
        flavors = ", ".join(self._flavors)
        size = self._size.capitalize()
        total = self.get_total()
        if len(self._flavors) == 0:
            return f"{size} {base} - {total}"
        else:
            return f"{size} {base} with {flavors} - {total}"
    
# class Food:
#     available_items = {"hotdog", "corndog", "ice cream", "onion rings", "french fries", "tater tots", "nacho chips"} #a list of food items offered by Cinos
#     food_toppings = {"nacho cheese", "chili", "bacon bits", "ketchup", "mustard"} #a list of food toppings offered by Cinos
#     ice_cream_toppings = {"cherry", "whipped cream", "caramel sauce", "chocolate sauce"} #a list of ice cream toppings offered by Cinos
    
#     def __init__(self): #defines the initialization
#         self._item = None
#         self._toppings=[]
    
#     def get_item(self): #gets the item of the Food object
#         return self._item
    
#     def get_toppings(self): #gets the list of toppings in the Food object
#         toppings_list = []
#         for topping in self._toppings:
#             toppings_list.append(topping)
#         return toppings_list
    
#     def get_num_toppings(self): #gets the number of toppings in the Food object
#         return len(self._toppings)
    
#     def get_total(self): #calculates the total of the Food object it is used on
#         item_cost = 0
#         toppings_cost = 0
#         #calculates the cost of the item
#         if self._item == "hotdog": item_cost = 2.30
#         elif self._item == "corndog": item_cost = 2.00
#         elif self._item == "ice cream": item_cost = 3.00
#         elif self._item == "onion rings": item_cost = 1.75
#         elif self._item == "french fries": item_cost = 1.50
#         elif self._item == "tater tots": item_cost = 1.70
#         elif self._item == "nacho chips": item_cost = 1.90
#         else: Exception("Error calculating total, invalid item")
#         #calculates the cost of the toppings
#         for topping in self._toppings:
#             if topping == ("caramel sauce" or "chocolate sauce"):
#                 toppings_cost += 0.50
#             elif topping == ("nacho cheese" or "bacon bits"):
#                 toppings_cost += 0.30
#             elif topping == "chili":
#                 toppings_cost += 0.60
#         #calculates the final cost
#         return item_cost + toppings_cost
        
    
#     def set_item(self, item): #sets the item of the Food object
#         if item.lower() in Food.available_items:
#             self._item = item
    
#     def add_topping(self, topping): #adds a topping to the list of toppings in the Food object 
#         if self._item == "ice cream":
#             if topping.lower() in Food.ice_cream_toppings:
#                 self._toppings.append(topping)
#             elif topping.lower() in Food.food_toppings:
#                 raise Exception("This topping is only available for food items.")
#             else: raise Exception("ERROR")
#         else:
#             if topping.lower() in Food.ice_cream_toppings:
#                 raise Exception("This topping is only available for ice cream.")
#             elif topping.lower() in Food.food_toppings:
#                 self._toppings.append(topping)
#             else: raise Exception("ERROR")
    
#     def set_toppings(self, toppings): #initialize with an array of toppings, sets the toppings of the Food object
#         for topping in toppings:
#             if topping.lower() in (Food.food_toppings or Food.ice_cream_toppings):
#                 self.add_topping(topping)
                
#     def __str__(self): #defines the string that is passed as the description of the Food object
#         item = self._item.title()
#         toppings = ", ".join(self._toppings)
#         total = self.get_total()
#         if len(self._toppings) == 0:
#             return f"{item} - {total}"
#         else: 
#             return f"{item} with {toppings} - {total}"

# class Order:    
    
#     def __init__(self): #defines the initialization of the Order object, uses a list of Drink/Food objects
#         self._items = []
    
#     def get_items(self): #gets the list of items in the Order object
#         return self._items.copy()
    
#     def get_num_items(self): #gets the number of items in the Order object
#         return len(self._items)
    
#     def get_total(self): #calculates the total of the Order object
#         total = 0
#         for item in self._items:
#             if isinstance(item, Drink): #checks if the current item is a Drink object
#                 total += Drink.get_total(item) #uses the Drink get_total method with the item
#             elif isinstance(item, Food): #checks if the current item is a Food object
#                 total += Food.get_total(item) #uses the Food get_total method with the item
#         tax = round(total * 0.0725, 2)
#         return total + tax
        
#     def get_receipt(self): #generates the receipt data, and includes \n for formatting purposes
#         receipt_lines = ["Cinos Sales Receipt"]
#         for drink in self._items:
#             receipt_lines.append(str(drink))
#         total = self.get_total()
#         receipt_lines.append(f"Total including tax: ${total:.2f}")
#         return "\n".join(receipt_lines)
        
#     def add_item(self, item): #adds a Drink object to the list of items in the Order object
#         self._items.append(item)
    
#     def remove_item(self, index): #removes an item from the list of items in the Order object at the specified index
#         if 0 <= index < len(self._items):
#             del self._items[index]