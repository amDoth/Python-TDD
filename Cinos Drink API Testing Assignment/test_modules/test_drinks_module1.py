from API_classes.drinks import Drink
from API_classes.order import Order
import pytest
    
def test_base_getter_setter():
    """ Test drink base getter and setter functions in the Drink class"""
    drink = Drink("small")
    drink.set_base("water")
    assert drink.get_base() == "water" #to test the set_base and get_base methods
    
def test_flavor_methods():
    """ Test drink flavor getter, setter, and adder functions in the Drink class """
    drink = Drink("small")
    drink.set_flavors(["lemon", "strawberry"])
    assert drink.get_flavors() == ["lemon", "strawberry"] #to test the set_flavors method
    assert drink.get_num_flavors() == 2 #to test the get_num_flavors method
    drink.add_flavor("blueberry")
    assert drink.get_num_flavors() == 3 #to test the add_flavor method
    
def test_order_drink_items_methods():
    """ Test the methods dealing with Drink items in the Order class"""
    drink1 = Drink("small")
    drink1.set_base("sbrite")
    drink1.set_flavors(["strawberry", "lime"])
    
    drink2 = Drink("small")
    drink2.set_base("hill fog")
    drink2.add_flavor("blueberry")
    
    order = Order()
    order.add_item(drink1) #to test the add_item method
    order.add_item(drink2)
    
    items = order.get_items()
    
    assert items == order._items #to test the get_items method
    assert order.get_num_items() == 2 #to test the get_num_items method
    
    order.remove_item(1)
    
    assert order.get_num_items() == 1 #to test the remove_item method and further test the get_num_items method
    
def test_receipt_method():
    """Test the method to generate the receipt"""
    drink = Drink("small")
    drink.set_base("pokeacola")
    drink.add_flavor("blueberry")
    
    order = Order()
    order.add_item(drink)
    
    assert order.get_receipt() =="Cinos Sales Receipt\nSmall pokeacola with blueberry - 1.65\nTotal including tax: $1.77" #to test the get_receipt method
    
    