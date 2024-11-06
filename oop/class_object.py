class Student:
    # name = "karan"

    college = "IIT Madras"  # class attributes

    name = "anonymous"

    # default constructors
    # def __init__(self):
    #     pass

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name  # instant/object attributes
        self.marks = marks
        # print("Creating new student")

    def hello(self):
        print("Welcome student", self.name)

    def get_marks(self):
        return self.marks


# everything's related to student s1
s1 = Student("Riyaz", 93)
print(s1)
print(s1.name)
print(s1.college)
print(Student.college)
print(s1.name)
print(s1.hello())
print(s1.get_marks())

# everything's related to student s1
s2 = Student("Mehak", 88)
print(s2)
print(s2.name)


# class car object
class Car:
    color = "blue"
    brand = "mercedes"


car1 = Car()
print(car1.color)
