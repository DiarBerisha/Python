class Person:
    def __init__(self, emri, mbiemri, mosha):
        self.emri = emri
        self.mbiemri = mbiemri
        self.mosha = mosha

    def greet(self):
        print("The persons name is: ", self.emri,"the persons surname is :", self.mbiemri, "the persons age is :", self.mosha)
person1 = Person("Diar", "Berisha", "17")
person2 = Person("Donart", "Sefa", "17")

print(person1.greet())
print(person2.greet())