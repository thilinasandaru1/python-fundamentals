# A Tuple is a collection which is ordered and unchangeable. 
# Allows duplicate members.


# create tuple
fruits = ('Apple', 'Orange', 'Mango')

# create tuple using a contructor
fruits2 = tuple(('Apple', 'Orange', 'Mango'))

# get value
print(fruits[1])

# cannot change value , uncomment to get an error
# fruits[1] = 'Grape'

# if tuple have only one value, we should use traling comma
fruits3 = ('Apple',)

# get length
print(len(fruits))

# delete tuple
del fruits3