grades = {
    ("John", "Math"): 5,
    ("Alice", "Sience"): 4,
    ("Bob", "History"): 3
}

john_math = grades[("John", "Math")]
print(john_math)

grades[("Alice","Sience")]=5
print(grades("Alice", "Sience"))

keys = list(grades.keys())

student, subject = keys[0]
print("First key - Student:", student, ",Subjekt:", subject)