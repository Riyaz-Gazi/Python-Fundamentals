# Used to delete object properties or object itself

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Riaz")
print(s1.name)
del s1
# print(s1)
