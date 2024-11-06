class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod   # decorator
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        avg = sum / 3
        print("Hi", self.name, "your avg score is ", avg)


s1 = Student("Tony Stark", [99, 98, 97])
s1.get_avg()
s1.name = "Iron Man"
s1.get_avg()
s1.hello()
