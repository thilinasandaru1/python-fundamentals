# JSON is commonly used with data APIs.

import json

# example JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# parse JSON to dictionary
user = json.loads(userJSON)

print(user)

# parse dictionary to JSON
userJSON2 = json.dumps(user)

print(userJSON2)
