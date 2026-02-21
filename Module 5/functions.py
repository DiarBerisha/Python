# def greet():
#     print("hello world")
# greet()
#
# def greet_person(name):
#     print("Hello", name)
#
# greet_person("Diar")
#
# def greet2(name):
#     message = f"hello, {name}"
#     print(message)
#
# greet2("Diar")
#
# greeting = "Hello"
# name = "Diar"
#
# def greet():
#     global greeting
#     greeting = "Goodbye"
#
#     name = "Donart"
#
#     message = f"{greeting}, {name}"
#     print(message)
#
# greet()



def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}"
    return message

metoda1 = greet_person("Diar")
metoda2 = greet_person("Donart", "Hi")
print(metoda1)
print(metoda2)