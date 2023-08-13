# integer
x = 1
y = 2 

# Case Sensitivity name and Name is different with each other - single quotes and double quotes are fine
name = "Jasper"
Name = 'Ira'

# float
pi = 3.14

# Assign variables with different values
a, b, c = "Alphabet A", "Alphabet B", "Alphabet C"
# Assign variables with same values
d = e = f = "Alphabet"

# Unpack Collection
fruits = ["Manga", "Apple", "Orange"]
firstFruit, secondFruit, thirdFruit = fruits

""""
Legal Variables
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal Variables
2myvar = "John"
my-var = "John"
my var = "John"

Camel Case - camelCase
Pascal Case - PascalCase
Snake Case - snake_case
"""

# Concatination or addition (+) - in python you cant add string and number unless you change the datatype but has weird value if you change it
print(x + y)
print(Name)

# type() - function used to know the data type
print(type(x))
print(type(name))
print(type(pi))

print(b)
print(f)

print(secondFruit)

# You can print multiple values in print() function
print(firstFruit, secondFruit, thirdFruit)
# Does the same as above but it does not create 1 whitespace
print(firstFruit + secondFruit + thirdFruit) 

print(name, x) #Output: Jasper 1 - you can print string and number if you do like this

# Global Variables
# city = "Caloocan City" # You can access this variable anywhere

def myFunction():
    # However if the variable is inside the function it is not accessible outside of the function
    global city
    city = "Malabon City" # to set this global use - global keyword to access outside
    print("Mabuhay ka " + city)

myFunction()
print("Mabuhay ka", city)