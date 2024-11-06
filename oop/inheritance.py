# when one class (child/derived) derives the properties & methods of another class(parent/base)

# single inheritance
# Multi-level inheritance
# Multiple inheritance
class Car:

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stop...")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")
#
# print(car1.brand)
# print(car1.start())

car1 = Fortuner("diesel")
car1.start()
