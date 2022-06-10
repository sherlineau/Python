
class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self,percent_change, is_increased):
        if(is_increased):
            self.price = self.price + (self.price * (percent_change/100)) 
        else:
            self.price = self.price - (self.price * (percent_change/100))

    def print_info(self,):
        print(f"Item: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Category: {self.category}")

# apple = Product('apple', 1.0, 'produce')
# apple.print_info()
# apple.update_price(3,True)
# apple.print_info()