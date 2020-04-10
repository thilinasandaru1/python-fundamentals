# A dictionary is a collection which is unordered, changeable and indexed
# No duplicate members.

# create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# create dictionary using a constructor
person2 = dict(
    first_name='John',
    last_name='Doe',
    age=30
)

# get value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-5555'

# get keys 
print(person.keys())

# get items
print(person.items())

# make a copy
person3 = person.copy()

# remove item
del(person['age'])
person.pop('phone')

# clear whole dictionary
person.clear()

# get length
print(len(person3))

# list of dictionary
people = [
    {'name': 'John', 'age': 30},
    {'name': 'Ross', 'age': 27},
    {'name': 'Monica', 'age': 28}
]

print(people[1]['name'])