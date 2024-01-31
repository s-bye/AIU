# Code to check
myfamily = ("mother", "father", "sister", "brother", "sister")
print(myfamily)

# 1 Task
print(type(myfamily)) # Output: <class 'tuple'>

# 2 Task
print(myfamily[2]) # Output: sister
# To access elements within a tuple, we can use indexing

# 3 Task
# myfamily.append('me') # We cannot, because it will cause error "AttributeError: 'tuple' object has no attribute 'append'"
# This proves that the 'tuple' data type is immutable and we cannot add, remove or modify items
# To check code, remove the first '#' in 10th line
# However, there is a trick by which we can add, modify and delete items in the 'tuple'.
templst = list(myfamily) # Let's create a new variable to make 'myfamily' a list
templst.append('me') # Adding 'me' item into list
myfamilyandme = tuple(templst) # Now we make 'myfamilyandme' back into tuple
print(myfamilyandme) # Output: ('mother', 'father', 'sister', 'brother', 'sister', 'me')

# 4 Task
# myfamily.pop(3) # We cannot, because it will cause error "AttributeError: 'tuple' object has no attribute 'pop'"
# Again, this proves the immutability of the 'tuple' data type
# To check code, remove the first '#' in 23rd line
# Here we can also use the trick from task 3
templist = list(myfamily) # Let's create a new variable to make 'myfamily' a list
templist.pop(3) # Removing 'brother' item from the list
myfamilywithoutbrother = tuple(templist) # Now we make 'myfamilywithoutbrother' back into tuple
print(myfamilywithoutbrother) # Output: ('mother', 'father', 'sister', 'sister')