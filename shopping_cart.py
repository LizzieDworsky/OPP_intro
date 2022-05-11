from product import Product


class ShoppingCart:
    def __init__(self):
        self.cart_contents = []
    
    def amount_currently_in_cart (self):
        total = len (self.cart_contents)
        return total
    
    def add_product_to_cart (self, product_name, product_price, product_category):
        self.cart_contents.append (Product(product_name, product_price, product_category))
    
    def empty_the_cart (self):
        self.cart_contents = []