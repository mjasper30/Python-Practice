people = ("Jasper", "Ira", "Poppy", "Jasper")
# person[0] = "Jasper"  # error because you cannot change the value

# this will not recognize as tuple unless you add comma in the end
person = ("Jasper")
person1 = ("Jasper",)

# can combine any datatype
tuple1 = ("abc", 34, True, 40, "male")

# tuple constructor
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))

print(people)
print(len(people))
print(len(person))
print(len(person1))

print(type(person))
print(type(person1))

"""
*Set items are unchangeable, but you can remove and/or add items whenever you like.

*As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

"""
