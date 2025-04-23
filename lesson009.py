class Employee:

    def employeeData(self):
        self.name = "Paul"
        print(self.name)

        salary = 5000
        print(salary)

    def getData(self):
        print(self.name)
        #print(salary)

paul = Employee()
paul.employeeData()
paul.getData()
