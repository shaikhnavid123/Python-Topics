class Employee:
    var = 8
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
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("This is good " + string)
        return #"Yes"

class Player:
    var = 9
    no_of_games = 5
    def __init__(self, name, game):
        self.name = name
        self.game = game
    def printdetails(self):
        return f"Name is {self.name}. Game is {self.game}."

# elliot = Employee("Harry", 4554, "Cyber Security Expert")
# alderson = Employee("Alderson", 6465, "Technical Staff")
# rami = Employee.from_dash("Rami-5825-Instructor")

class CoolProgrammer(Employee, Player):
    # var = 10
    language = "C++"
    def printlanguage(self):
        print(self.language)
        # return f"Name is {self.name}.Salary is {self.salary}. Role is {self.role} Game is {self.game}."

allen = ["Allen", ["Chess"]]
barry = CoolProgrammer("Barry", 5457, "CoolProgrammer")
det = barry.printdetails()
print(det)
barry.printlanguage()
print(barry.var)