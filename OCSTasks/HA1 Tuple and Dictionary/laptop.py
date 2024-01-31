# Code to check
laptop = { "brand": "dell", "model": "alienware", "year": 2010 }
# A dictionary is an unordered data structure that allows you to store key-value pairs

# 1 Task
# Square brackets [] are used to get the value of a particular key
print(laptop["brand"])# Output: dell

# 2 Task
# Add the key "home" with the meaning "True", which is a boolean data type
laptop["home"] =True  # Adding a new value "home" with the meaning "True"
print(laptop["home"]) # Output: True
print(type(laptop["home"])) # Output: <class 'bool'>

# 3 Task
# Update the "year" key and set it to "2019"
laptop["year"] = '2019' # Updating the "year" key and changing value to "2019"
print(laptop["year"]) # Output: 2019
