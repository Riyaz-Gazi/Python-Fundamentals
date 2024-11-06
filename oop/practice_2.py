class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role :", self.role)
        print("dept : ", self.dept)
        print("salary : ", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        # super().__init__(role, dept, salary)
        super().__init__("Engineer", "IT", "75,0000")
        self.name = name
        self.age = age


e1 = Employee("accountant", "finance", "60000")
e1.showDetails()
e2 = Engineer("Elon", 25)
e2.showDetails()
