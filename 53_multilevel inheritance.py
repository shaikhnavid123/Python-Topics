class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    # basketball = 5
    def isdance(self):
        return f"Yes I dance {self.dance} no. of times."

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Jackson Yeah! "\
            f"Yes I dance {self.dance} no. of times."
    # def isdance(self):
    #     return f"Jackson Yeah! "\
    #         f"Yes I dance {self.dance} no. of times."
darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)


#------------------------ ---------EXERCISE-----------------------------------------#

class Electronic_Device:
    wifi_dongle = 1

class Pocket_Gadget(Electronic_Device):
    lighter = 3
    samsung = 2
    canwork = 2
    def canworkfor(self):
        return f"It can work for {self.canwork} hours in a day."

class Phone(Pocket_Gadget):
    samsung = 5
    canwork = 6
    def canworkfor(self):
        return f"It can work for {self.canwork} hours in a day."
    # canwork = 6
    # def canworkfor(self):
    #     return f"It can work for {self.canwork} hours in a day."

device = Electronic_Device()
gadget = Pocket_Gadget()
smartphone = Phone()

print(smartphone.canworkfor())
print(smartphone.canwork)
print(Phone.lighter)
print(Phone.samsung)
print(gadget.canworkfor())