from shopping_cart import ShoppingCart


#As a developer, I want the Customer class to have a method to view all products in the customer’s shopping cart. (Loop over the shopping cart’s products list and print each product to the terminal)



class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart ()
    
    def add_to_cart (self, product_name, product_price, product_category):
        self.cart.add_product_to_cart(product_name, product_price, product_category)
    
    def view_cart_contents (self,):
        for item in self.cart.cart_contents:
            print (item.name)