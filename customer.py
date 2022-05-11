from shopping_cart import ShoppingCart


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart ()
    
    def add_to_cart (self, product_name, product_price, product_category):
        self.cart.add_product_to_cart(product_name, product_price, product_category)
    
    def view_cart_contents (self,):
        for item in self.cart.cart_contents:
            print (item.name)