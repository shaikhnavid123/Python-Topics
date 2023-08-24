# OOPS - Object Oriented Programming
# Classes - Template
# Object - Instance of the class
# DRY - Do not repeat yourself
# get_no_of_films(srk) - appropriate
# get_no_of_films(table) - inappropriate

class Student:
    pass

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["Maths", "Science"]

print(harry, larry)
print(harry.name)
print(harry.std, larry.std)
print(harry.section, larry.subjects)
# print(larry.name) #error will pop-up



