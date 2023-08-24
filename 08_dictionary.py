#dictionary = {}
d0 = {}
print(type(d0))
d1 = {"Elliot":"Smart",
      "Mr.Robot":"Hacker",
      "Zenox":{"day":"White Hat", "night":"Black Hat"}}
print(d1)
print(d1["Mr.Robot"])
print(d1["Zenox"]["night"])

d1["Rami"] = "Software Engineer"
d1[101] = "CTO"
print(d1)

del d1[101]
print(d1)

d1.update({"Angela":"Programmer"})
print(d1.get("Mr.Robot"))
print(d1)
print(d1.keys())
print(d1.items())
"""
d2 = d1
del d2["Elliot"]
print(d1)
"""
d2 = d1.copy()
del d2["Elliot"]
print(d1)




