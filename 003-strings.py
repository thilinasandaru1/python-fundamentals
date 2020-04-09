# string can be sorrounded by either single quotes or double quotes

name = "Thilina"
age = 28

# Concatenate
print("I am " + name + " and I am " + str(age) + " yeas old")

# String Placeholder
print('{} {} {}'.format("Go", "for", "it"))
print('{1} {2} {0}'.format("you?", "How", "are"))
print('My name is {name} and I am {age} years old'.format(name="Thilina", age="28"))

# F Strings
print(f'My name is {name} and I am {age} years old')

''' STRING METHODS '''

s = 'lets be friends'

# Capitalize first letter
print(s.capitalize())

# Capitalize all letters
print(s.upper())

# Lowercase all letters
print(s.lower())

# Swap case
print(s.swapcase())

# Get Length
print(len(s))

# Replace
print(s.replace("friends", "buddies"))

# Count
print(s.count("e"))

# Start with
print(s.startswith("lets"))

# Ends with
print(s.endswith("ds"))

# Splits into a list
print(s.split())

# Find position
print(s.find("b"))

# is all alphanumeric - spaces return false
print(s.isalnum())

# is all alphabetic - spaces return false
print(s.isalpha())

# is all numeric
print(s.isnumeric())