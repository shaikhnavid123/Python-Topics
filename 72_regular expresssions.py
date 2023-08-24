import re
# functions : findall, search, split, sub, finditer

mystr = '''Name : Elliot Alderson
Phone : +44 (20) 7235 8281
Fax : +44 (20) 7235 872
Contact : 45984-84612
Email : elliotalderson@gmail.com
Directions : View map'''

# Meta Characters :

# pattern = re.compile(r'map')
# pattern = re.compile(r'.') # . Any Character (except new line character)
# pattern = re.compile(r'.son')
# pattern = re.compile(r'^Name') # ^ starts with
# pattern = re.compile(r'Name$') # $ Ends with
# pattern = re.compile(r'map$')
# pattern = re.compile(r'io*') # * Zero or occurrences
# pattern = re.compile(r'i*o*')
# pattern = re.compile(r'io+') # + One or more occurrences
# pattern = re.compile(r'io{1}') # {} Exactly the specified number of occurrences
# pattern = re.compile(r'(io){1}') # () Capture and group
# pattern = re.compile(r'io{1}|t') # | Either or
# pattern = re.compile(r'io{1}|Fax')

# Special Sequence :

# pattern = re.compile(r'\AName') # \A Starts with
# pattern = re.compile(r'\AFax')
# pattern = re.compile(r'\bFax')
# pattern = re.compile(r'Fax\b')
# pattern = re.compile(r'\d{5}-\d{5}')

matches = pattern.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[126:129])


#-----------------------Contact list-----------------------------#
#
# ind_contacts = '''
# 1 = +91-98746-88481
# 2 = +91-78454-84217
# 3 = +91-87651-87856
# '''
# pattern_num = re.compile(r'\d{2}-\d{5}-\d{5}')
#
# find = pattern_num.finditer(ind_contacts)
# for found in find:
#     print(found)