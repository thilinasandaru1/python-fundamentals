''' FOR LOOP '''
# A for loop is use for iterating over a sequence.

people = ['John', 'Will', 'Janet', 'Emma']

for person in people:
    print(person)

# break
for person in people:
    print(person)
    if person == 'Janet':
        break

# continue
for person in people:
    if person == 'Janet':
        continue
    print(person)

# range
for i in range(len(people)):
    print(people[i])
    
for i in range(0, 10):
    print(i)

''' WHILE LOOP '''
# while loop executes a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(count)
    count += 1
