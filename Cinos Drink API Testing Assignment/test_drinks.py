from drinks import Drink, Order
import pytest
    
def test_base_getter_setter():
    """ Test drink base getter and setter functions in the Drink class"""
    drink = Drink()
    drink.set_base("water")
    assert drink.get_base() == "water"
    
def test_flavor_methods():
    """ Test drink flavor getter, setter, and adder functions in the Drink class """
    drink = Drink()
    drink.set_flavors(["lemon", "strawberry"])
    assert drink.get_flavors() == ["lemon", "strawberry"]
    assert drink.get_num_flavors() == 2
    drink.add_flavor("blueberry")
    assert drink.get_num_flavors() == 3
    
def test_order_items_methods():
    """ Test the methods dealing with items in the Order class"""
    drink1 = Drink()
    drink1.set_base("sbrite")
    drink1.set_flavors(["strawberry", "lime"])
    
    drink2 = Drink()
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
    drink = Drink()
    drink.set_base("pokeacola")
    drink.add_flavor("blueberry")
    
    order = Order()
    order.add_item(drink)
    
    assert order.get_total() == 3.00
    assert order.get_receipt() =="Cinos Sales Receipt\npokeacola with blueberry\nSubtotal: $3.00\nTax: $0.20\nTotal: $3.20" 
    