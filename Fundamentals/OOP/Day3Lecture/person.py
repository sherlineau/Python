
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def print_info(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Age:", self.age)