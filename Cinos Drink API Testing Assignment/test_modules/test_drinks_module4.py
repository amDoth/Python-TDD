from API_classes.drinks import Drink
from API_classes.food import  Food
from API_classes.order import Order
from API_classes.ice_storm import Ice_Storm
import pytest

def test_ice_storm_flavor_and_toppings_methods():
    """ To test all of the flavor and toppings methods in the Ice_Storm class """
    ice_storm = Ice_Storm()
    ice_storm.set_flavor("smore")
    ice_storm.set_toppings(["dig_dogs", "cherry", "chocolate_sauce"])
    
    assert ice_storm.get_flavor() == "smore" #to test the get_flavor method (and set_flavor)
    assert ice_storm.get_toppings() == ["dig_dogs", "cherry", "chocolate_sauce"] #to test the get_toppings method (and set_toppings)
    assert ice_storm.get_num_toppings() == 3 #to test the get_num_toppings method
    
    ice_storm.remove_topping(1) #to test the remove_topping method
    ice_storm.add_topping("whipped_cream") #to test the add_topping method
    
    assert ice_storm.get_num_toppings() == 3 #to further test the get_num_toppings method
    assert ice_storm.get_toppings() == ["dig_dogs", "chocolate_sauce", "whipped_cream"] #to further test the get_toppings method
    
def test_ice_storm_total_method():
    """ To test the total method in the Ice_Storm class """
    ice_storm = Ice_Storm()
    ice_storm.set_flavor("chocolate")
    ice_storm.set_toppings(["cookie_dough","caramel_sauce"])
    
    assert ice_storm.get_total() == 4.50 #to test the get_total method
    
    ice_storm.add_topping("tnts")
    
    assert ice_storm.get_total() == 5.50 #to further test the get_total method

def test_ice_storm_order_methods():
    """ To test the Ice_Storm methods in combination with the Order methods"""
    
    ice_storm = Ice_Storm()
    ice_storm.set_flavor("butter_pecan")
    ice_storm.add_topping("cherry")
    
    order = Order()
    order.add_item(ice_storm)
    
    assert order.get_receipt() == "Cinos Sales Receipt\nButter Pecan ice storm with cherry - 3.50\nTotal including tax: $3.75"
    #^to test the get_receipt method from the Order class in combination with an item from the Ice_Storm class