from API_classes.drinks import Drink
from API_classes.food import Food
from API_classes.order import Order
import pytest

def test_food_item_getter_setter():
    """ Test the food item getter and setter methods """
    food = Food()
    food.set_item("hotdog") #to test the set_item method
    assert food.get_item() == "hotdog" #to test the get_item method
    
def test_topping_methods():
    """ Test the food topping setter, getter, and adder functions """
    food = Food()
    food.set_item("french fries") 
    food.set_toppings(["ketchup","chili"]) #to test the set_toppings method
    assert food.get_toppings() == ["ketchup", "chili"] #to test the get_toppings method
    assert food.get_num_toppings() == 2 #to test the get_num_toppings method
    food.add_topping("bacon bits")
    assert food.get_num_toppings() == 3 #to further test the get_num_toppings method
    with pytest.raises(Exception) as exc:
        food.add_topping("cherry")
    assert str(exc.value) == "This topping is only available for ice cream." 
    #^to test that an exception is raised when adding an ice cream topping to a food item
    
def test_order_food_items_methods():
    """ Test the methods dealing with Food items in the Order class """
    food1 = Food()
    food1.set_item("french fries")
    food1.add_topping("nacho cheese")
    
    food2 = Food()
    food2.set_item("ice cream")
    food2.set_toppings(["whipped cream", "caramel sauce"])
    
    food3 = Food()
    food3.set_item("corndog")
    
    order = Order()
    order.add_item(food1)
    order.add_item(food2)
    order.add_item(food3)
    
    assert order.get_items() == order._items #to test the get_items method with Food items
    assert order.get_num_items() == 3 #to test the get_num_items method with Food items
    
    order.remove_item(0) #to test the remove_item method with Food items
    
    assert order.get_num_items() == 2 #to further test the get_num_items and remove_item methods
    
def test_receipt_total_methods():
    """ Test the receipt and total calculation methods with Food items """
    food = Food()
    food.set_item("onion rings")
    
    assert food.get_total() == 1.75 #to test the get_total method
    
    drink = Drink("small")
    drink.set_base("mr. salt")
    drink.add_flavor("lime")
    
    order = Order()
    order.add_item(food)
    
    order.add_item(drink)
    
    assert order.get_receipt() == "Cinos Sales Receipt\nOnion Rings - 1.75\nSmall mr. salt with lime - 1.65\nTotal including tax: $3.65" 
    #^to test the get_receipt method with Food items
    
    food.add_topping("nacho cheese")
    
    assert food.get_total() == 2.05 #to test the get_total method after using the add_topping method
    