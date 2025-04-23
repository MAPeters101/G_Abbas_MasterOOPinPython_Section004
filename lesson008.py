class Employee:

    # Class attribute
    companyName = "ABC"

    # Using instance attributes here
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def showEmployeeDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Company:", self.companyName)

paul = Employee("Paul", 25, 5000)
paul.showEmployeeDetails()
print()

chris = Employee("Chris", 30, 10000)
chris.showEmployeeDetails()

