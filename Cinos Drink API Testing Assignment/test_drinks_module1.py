from drinks import Drink, Order
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
    
def test_drink_size_total_methods():
    """ Test drink size setter and getter functions and the total calculation function """
    drink = Drink("mega")
    assert drink.get_size() == "mega" #to test the get_size method
    drink.set_size("medium")
    assert drink.get_size() == "medium" #to test the set_size method
    drink.set_base("sbrite")
    drink.add_flavor("lemon")
    assert drink.get_total() == 1.90 #to test the get_total method
    drink.add_flavor("blueberry")
    assert drink.get_total() == 2.05 #to ensure each flavor adds $0.15
    
def test_order_items_methods():
    """ Test the methods dealing with items in the Order class"""
    drink1 = Drink("small")
    drink1.set_base("sbrite")
    drink1.set_flavors(["strawberry", "lime"])
    
    drink2 = Drink("small")
    drink2.set_base("hill fog")
    drink2.add_flavor("blueberry")
    
    order = Order()
    order.add_item(drink1)
    order.add_item(drink2)
    
    items = order.get_items()
    
    assert items == order._items
    assert order.get_num_items() == 2
    
    order.remove_item(1)
    
    assert order.get_num_items() == 1
    
def test_total_and_receipt_methods():
    """Test the methods to calculate the total and generate the receipt"""
    drink = Drink("small")
    drink.set_base("pokeacola")
    drink.add_flavor("blueberry")
    
    order = Order()
    order.add_item(drink)
    
    assert order.get_receipt() =="Cinos Sales Receipt\nsmall pokeacola with blueberry - 1.65\nTotal including tax: $1.77" 
    
    assert order.get_total() == 1.77
    