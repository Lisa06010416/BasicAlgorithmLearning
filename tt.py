import re

string = "hello 123abc"
r = re.search("1(2)(3.*)", string)

print(r)
print(r.span())    # (6, 12)
print(r.group())   # 123abc
print(r.group(1))  # 2
print(type(r.group(1)))  # 2
print(r.groups())  # ('2', '3abc')