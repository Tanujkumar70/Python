 ## Multiple Inheritance
class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"

    def printLanguage(self):
        print(f"Out of Languages, here is your Language: {self.language}")

class Programmer(Employee, Coder):
    company = "YouTube"

    def showLanguage(self):
        print(f"The name is {self.name} and they are good with the {self.language} language")

# Example usage:
a = Employee("Alice", 50000)
b = Programmer("Bob", 70000)

a.show()
b.show()
b.printLanguage()
b.showLanguage()
