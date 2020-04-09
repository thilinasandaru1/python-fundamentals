# A list is a collection which is ordered and changeable. A
# Allows duplicate members

# create list
numbers = [1,2,3,4,5]

# create list using a contructor
numbers2 = list((1,2,3,4,5))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# get value
print(fruits[1]) # Oranges

# length
print(len(fruits))

# append to list
fruits.append('Mangos')

# remove from list
fruits.remove("Grapes")

# Insert intio specific position
fruits.insert(2, 'Stawberries')

# Remove from position
fruits.pop(3)

# reverse list
fruits.reverse()

# sort
fruits.sort()

# sort -reverse
fruits.sort(reverse=True)

print(fruits)