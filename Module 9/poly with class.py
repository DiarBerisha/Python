class Dog():
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} make the sound:woof!")

class Cat():
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound : meow!")


class Bird():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound : Quack!")



dog = Dog("Bub")
cat = Cat("wisk")
bird = Bird("larry")

for animal in (dog, cat, bird):
    animal.sound()