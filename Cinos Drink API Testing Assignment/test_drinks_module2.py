from drinks import Drink, Order
import pytest

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
    
def test_total_method():
    """Test the method to calculate the total of the Order"""
    drink = Drink("small")
    drink.set_base("pokeacola")
    drink.add_flavor("blueberry")
    
    drink2 = Drink("Mega")
    drink2.set_base("sbrite")
    
    order = Order()
    order.add_item(drink)
    
    assert order.get_total() == 1.77 #to test the Order get_total method
    
    order.add_item(drink2)
    
    assert order.get_total() == 4.08 #to further test the Order get_total method after adding an additional item
    