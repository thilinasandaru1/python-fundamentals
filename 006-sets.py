# A set is a collection which is unordered and unindexed.
# No duplicate members.

# create set
fruits = {'Apple', 'Orange', 'Mango'}

# check if value is in the set
print('Apple' in fruits) # True
print('Apples' in fruits) # False

# add value to set
fruits.add('Grape')

# remove value from set
fruits.remove('Mango')

# clear whole set
fruits.clear()

# delete set
del fruits