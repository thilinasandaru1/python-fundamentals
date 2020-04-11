# A module is basically a file containing a set of functions to include in your
# application. 
# There are core python modules.
# You can install modules via pip.

# core modules
# import datetime
from datetime import date

# today = datetime.date.today()
today = date.today()
print(today)


# custom module
import validator

email = "test@gmail.com"

if validator.validate_email(email):
    print('Valid Email')
else:
    print('Email is not Valid')
