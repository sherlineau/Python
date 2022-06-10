
class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.type = type

    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping! -- {self.name} gained 25 energy")

    def eat(self, food):
        self.energy += 5
        self.health += 10
        print(f"Feeding {self.name} some {food} -- {self.name} gained 5 energy and 10 health")

    def play(self):
        self.health += 5
        print(f"Played with {self.name} -- {self.name} gained 5 energy")


class Cat(Pet):

    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
        self. type = 'cat'

    def noise(self):
        print("meowww")


class Dog(Pet):

    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
        self. type = 'dog'

    def noise(self):
        print("woooofffff")
