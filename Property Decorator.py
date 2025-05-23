#Property Decorator

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The Class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

# Example usage:
e = Employee()
e.a = 45

# Initialize fname and lname before using the name property
e.name = "Tanuj Kumar"
print(e.name)
e.show()
