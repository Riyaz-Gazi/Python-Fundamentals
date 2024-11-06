# three type of methods
# static method
# class method
# instance method

class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     self.__class__.name = name
    # Person.name = name
    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Rahul")
print(p1.name)
print(Person.name)


# property decorator

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    # def calculatePercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


s1 = Student(99, 98, 97)
print(s1.phy)
print(s1.percentage)
s1.phy = 89
print(s1.percentage)
