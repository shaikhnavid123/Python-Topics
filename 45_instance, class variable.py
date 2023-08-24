class Employee:
    no_of_leaves = 8
    pass

elliot = Employee()
alderson = Employee()

elliot.name = "Elliot"
elliot.salary = 4564
elliot.role = "Cyber Security Expert"

alderson.name = "Alderson"
alderson.salary = 4525
alderson.role = "Technical Staff"

print(elliot.name)
print(alderson.role)
print(elliot.no_of_leaves)
print(alderson.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves = 9
print(Employee.no_of_leaves)
elliot.no_of_leaves = 10
print(elliot.no_of_leaves)
alderson.no_of_leaves = 8
print(alderson.__dict__)
print(Employee.__dict__)
Employee.no_of_leaves = 10
print(elliot.no_of_leaves)
print(Employee.__dict__)


