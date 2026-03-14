class Student:



    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return  self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__name = age


student1  = Student("nita",18)

print("Name: ",student1.get_name())
student1.set_name("Diar")
print("UpdatedName: ",student1.get_name())


print("age: ",student1.get_age())
student1.set_age(2)
print("Updatedage: ",student1.get_age())