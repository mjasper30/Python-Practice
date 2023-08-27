fruits = {"orange", "banana", "mango", "mango"}
# both True and 1 are the same
thisset = {"apple", "banana", "cherry", True, 1, 2}

# note the double round-brackets
constructor_thisset = set(("apple", "banana", "cherry"))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(fruits)
print(thisset)
print(type(fruits))
print(len(fruits))
print(constructor_thisset)
