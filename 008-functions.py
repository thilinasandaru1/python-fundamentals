# A function is block of code which only runs when it is called.
# In python, we do not use parenthese and curly brackets,
# we use indentation with tabs or spaces.

# create function
def sayHello(name = "Sam"):
    """
    print Hello and name
    """
    print('Hello ' + name)

sayHello('Thilina')

# return value
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(8, 10))

'''  LAMBDA FUNCTIONS  '''
# A lambda function is a small anonymous function.
# A lambda fuinction can take any number of arguments, but can only have one
# expression. Very similar to JavaScript arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(5, 4))