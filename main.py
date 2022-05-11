from alarm_clock import AlarmClock
from customer import Customer


first_customer = Customer ("Dani")
print (first_customer.name)
first_customer.add_to_cart ("detergent", 20, "cleaning")
first_customer.add_to_cart ("lotion", 5, "toiletries")
first_customer.add_to_cart ("conditioner", 8, "toiletries")
first_customer.view_cart_contents ()
product_total = first_customer.cart.amount_currently_in_cart ()
print (product_total)
product_total = first_customer.cart.empty_the_cart ()
print (product_total)



alarm_clock_one = AlarmClock()
alarm_clock_one.update_current_time()
print (alarm_clock_one.current_time)
alarm_clock_one.turn_alarm_on_off()