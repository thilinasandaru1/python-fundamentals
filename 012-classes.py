# A class is like blueprint for creating objects.
# An object has properties and methods associated with it.

# create class
class User:
    # contructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    #methods
    def greetings(self):
        return f'Name is {self.name}'


# initialize user object using class
thilina = User('PRT', 'me@prt.com', 27)
wick = User('John Wick', 'wick@john.com', 35)

# edit property
thilina.age = 28

print(thilina.greetings())

# extend class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance

    # override methods
    def greetings(self):
        return f'Name is {self.name} and also a customer'

# initialize
john = Customer('John Doe', 'john@doe.com', 25)

john.set_balance(500)

print(john.greetings())