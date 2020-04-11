# Python has functions for creating, reading, updating and deleting files.

# open a file
myFile = open('myfile.txt', 'w')


# get some info
print('File name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode:' ,myFile.mode)

# write to file
myFile.write('I love python')
myFile.close()

# append to file
myFile = open('myfile.txt', 'a')
myFile.write(' and Javascript')
myFile.close()

# read
myFile = open('myfile.txt', 'r+')
text = myFile.read(10)
print(text)