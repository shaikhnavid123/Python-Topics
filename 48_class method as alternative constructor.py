class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. And role is {self.role}"
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    @classmethod
    def from_dash(cls, string):
        # malek = string.split("-")
        # print(malek)
        # return cls(malek[0], malek[1], malek[2])
        return cls(*string.split("-"))

elliot = Employee("Harry", 4554, "Cyber Security Expert")
alderson = Employee("Alderson", 6465, "Technical Staff")
rami = Employee.from_dash("Rami-5825-Instructor")

# Employee.change_leaves(34)
# alderson.change_leaves(34)
# print(alderson.change_leaves)
# print(elliot.no_of_leaves)

print(rami.role)
print(rami.printdetails())
