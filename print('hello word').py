import re

test_string = "Name : Max. Birthdate : 18 July, 1998"
reg = r"Name : ([a-zA-Z]+)\. Birthdate : (\d+) ([a-zA-Z]+), (\d+)"
match = re.search(reg,test_string)

print(match.group(1,2,3,4))

p= 32
