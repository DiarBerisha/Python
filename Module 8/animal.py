class Animal:
    def __init__(self, typeOfAnimal, race, ngjyra):
        self.typeOfAnimal = typeOfAnimal
        self.race = race
        self.ngjyra = ngjyra

    def greet(self):
        print("The type of animal is:", self.typeOfAnimal, "The race is:", self.race, "The color is:", self.ngjyra)

dog = Animal('dog', "husky", "white")
cat = Animal('cat', "keqe", "white")

print(dog.greet())
print(cat.greet())