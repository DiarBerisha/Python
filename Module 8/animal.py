class Animal:
    def __init__(self, typeofanimal, race, ngjyra):
        self.typeofanimal = typeofanimal
        self.race = race
        self.ngjyra = ngjyra

    def greet(self):
        print("The type of animal is:", self.typeofanimal, "The race is:", self.race, "The color is:", self.ngjyra)

dog = Animal('dog', "husky", "white")
cat = Animal('cat', "keqe", "white")

print(dog.greet())
print(cat.greet())