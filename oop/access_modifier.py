class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("12345", "abcde")

print(acc1.acc_no)


# print(acc1.acc_pass)


class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello")

    def welcome(self):
        self.__hello()


p1 = Person()
# print(p1.__name)
p1.welcome()
