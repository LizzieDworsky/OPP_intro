

#As a developer, I want to import the Customer and Product classes into main.py so I can instantiate a customer object as well as three Product objects and interact with the object’s methods:
#1. Print the customer’s name to the terminal
#2. Call the customer’s add product to shopping cart method three times and add the three products objects you created
#3. Call the customer’s view products method
#4. Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal
#5. Call the customer’s shopping cart’s empty cart method
#6. Check if all products have been removed from the shopping cart
from alarm_clock import AlarmClock
from product import Product
from shopping_cart import ShoppingCart


my_cart = ShoppingCart ()
my_cart.add_product_to_cart ("Detergent", 20, "Cleaning")
print (my_cart.cart_contents)
my_cart.empty_the_cart()
print (my_cart.cart_contents)






























alarm_clock_one = AlarmClock()
alarm_clock_one.update_current_time()
print (alarm_clock_one.current_time)
alarm_clock_one.turn_alarm_on_off()