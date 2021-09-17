
"""---------- ord ----------"""
# ord() expected **a character**, but string of length 2 found
for i in range(0,9):
    print(ord(str(i)))

"""---------- type check ----------"""
# type
print(type({}), type(dict), type(dict()), dict) # <class 'dict'> <class 'type'> <class 'dict'> <class 'dict'>
print(type({}) == dict) # True
print(type({}) == type(dict)) # False

# isinstance
print(isinstance({}, dict)) # True
