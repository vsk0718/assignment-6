class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name} has a {self.coat_color} coat.")


class JackRussellTerrier(Dog):
    def bark(self):
        print("Woof! Woof!")

    def hunt(self):
        print("I love to eat Chicken!")


class Bulldog(Dog):
    def bark(self):
        print("Woof!")

    def snore(self):
        print("Zzzzzzzz...")

dog1 = Dog("Brownniieee", 4, "Brown")
dog1.description()
dog1.get_info()

dog2 = JackRussellTerrier("Elsa", 2, "Grey")
dog2.description()
dog2.get_info()
dog2.bark()
dog2.hunt()

dog3 = Bulldog("Nayra", 3, "Black and White")
dog3.description()
dog3.get_info()
dog3.bark()
dog3.snore()
