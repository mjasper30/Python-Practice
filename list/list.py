"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered** and changeable. No duplicate members.

! *Set items are unchangeable, but you can remove and/or add items whenever you like.

! **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

? When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.
"""


# List items are ordered, changeable, and allow duplicate values.
# index       0          1       2       3
fruits = ["Orange", "Banana", "Apple", "Apple",
          1, True]  # mix datatype values doesnt matter
age = [20, 21, 22]
condition = [True, False, False]

# Creating list constructor using list()
myList = list(("First Value", "Second Value", "Third Value"))

print(fruits)
print(condition)

# Check the length of the list
print(len(fruits))

# Check the datatype
print(type(fruits))

print(myList)
