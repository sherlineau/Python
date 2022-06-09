from pet import Cat, Dog, Pet

class Ninja:

    def __init__(self, first_name, last_name, petname, type, tricks):
        self.first_name = first_name
        self.last_name = last_name
        if type == 'dog' or type == 'Dog':
            self.pet = Dog(petname, type, tricks, health = 10, energy = 0)
        elif type == 'cat' or type =='Cat': 
            self.pet = Cat(petname, type, tricks, health = 10, energy = 0)
        else: 
            self.pet = Pet(petname, type, tricks, health = 10, energy = 0)

    def print(self):
            print(type(self.pet.health))

    def walk(self): #play
        self.pet.play()
        return self

    def feed(self,food): #eat
        self.pet.eat(food)
        return self

    def bathe(self): #noise
        self.pet.noise()
        return self

    def print_pet_info(self):
        print(f"{self.first_name}'s pet is at {self.pet.type} and their name is {self.pet.name}.")



sherline = Ninja("Sherline", "Au", "Lily", "cat", "knocking stuff over for food")
sherline.print_pet_info()
sherline.walk().feed("treats").bathe()

linda = Ninja("Linda", "Nguyen", "Wong Choi", "Dog", "rolling over")
linda.walk().feed("steak").bathe()

sherline.pet.sleep()