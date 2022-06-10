
from classes.product import Product

class Store:
    
    def __init__(self, name):
        self.name = name
        self.products = []

    # takes a product and adds it to the store
    def add_new_product (self, productname, price, category):
        self.products.append(Product(productname,price,category))

    # remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info
    def sell_product (self, i):
        index = self.products[i]
        print("Sold")
        index.print_info()

    #increases the price of each product by the percent_increase given
    def inflation(self, i, percentage):
        index = self.products[i]
        index.update_price(percentage, True)
        index.print_info()

    #updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
    def clearance(self, category,percentage):
        for x in range (0, len(self.products)):
            if self.products[x].category == category:
                self.products[x].update_price(percentage, is_increased=False)
                self.products[x].print_info()

    def print_all_products(self):
        print(f"Products available at {self.name}")
        for _ in range (0, len(self.products)):
            self.products[_].print_info()

