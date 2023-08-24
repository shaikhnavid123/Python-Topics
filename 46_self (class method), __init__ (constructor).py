class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. And role is {self.role}"
    # pass

elliot = Employee("Harry", 4554, "Cyber Security Expert")
# alderson = Employee()
#
# elliot.name = "Elliot"
# elliot.salary = 4564
# elliot.role = "Cyber Security Expert"
#
# alderson.name = "Alderson"
# alderson.salary = 4525
# alderson.role = "Technical Staff"


print(elliot.salary)
print(elliot.printdetails())