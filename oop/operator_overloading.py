print(1 + 2)
print("Riaz " + "Gazi")  # concatenate
print([1, 2, 3] + [2, 3, 4])  # mergea


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


c1 = Complex(2, 3)
c1.show()

c2 = Complex(4, 5)
c2.show()

# c3 = c1.add(c2)
# c3.show()
c3 = c1+c2
c3.show()
