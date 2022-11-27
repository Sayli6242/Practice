"""
# example for program pattern builder.


"""


def processSalary(name, role, salary):
    print(name, role, salary)


def getSalary():
    return 10


def getName():
    return "Ace"


def getROle():
    return "dev"


def main():
    for i in range(100):

        emp = Employee(i, i, i)
        print(emp.processSal())


class Employee:
    def __init__(self, name, role, salary, bonus) -> None:
        self.name = name
        self.role = role
        self.salary = salary
        self.bonus = bonus

    def processSal(self):
        return self.salary + self.bonus


main()
