import json

data = '{"var1":"elliot", "var2":"56"}'
print(data)

parsed = json.loads(data)
print(parsed)
print(type(parsed))

data2 = {
    "languages": ['python', 'javascript', 'C++'],
    "cars": ('bmw', 'audi', 'ferrari'),
    "isfine": False
}

print(data2["languages"])

jscomp = json.dumps(data2) # this is used for making python code compatible to javascript code
print(jscomp)