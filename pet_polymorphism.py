class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "Says bark")

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "says meow meow")

opet1 = Dog("Johny")
opet2 = Cat("Timi")

for pet in [opet1, opet2]:
    pet.speak()