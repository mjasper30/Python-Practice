# Create Class
class Person:
    name = "Jasper"

# Create a Class with __init__ - __init is like a constructor - automatically called when the class is declared


class Pet:
    def __init__(self, type, color):
        self.type = type  # <- property
        self.color = color  # <- property


# Create a class with __str__ used for formating text once the class is called
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        return f"Hello my name is {self.name} and my course is {self.course}"


# Create a class with methods inside
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def sayBrandName(self):
        print("My car is " + self.brand +
              " and the color of my car is " + self.color)

# Create a class other words from self - the self keyword used to reference the current state of the class and then access all the variables within that class


class Bottle:
    def __init__(myobject, bottle_name, size):
        myobject.bottle_name = bottle_name
        myobject.size = size

    def bottleCalling(abc):
        print("My plastic bottle is " + abc.bottle_name +
              " and the size is " + abc.size)


class Test:
    pass


# Create an Object
first_person = Person()
print(first_person.name)


# Create an Object from a class
pet = Pet("dog", "brown")
print(pet.type)
print(pet.color)

# Create an Object from a class
student = Student("Jasper Macaraeg", "BSCS")
print(student)

# Create an Object from class
car = Car("Toyota", "red")
car.sayBrandName()

# Create an Object from class
bottle = Bottle("C2", "Large")

# Modify the value
bottle.bottle_name = "Coke"
bottle.size = "Small"

# Delete an Object Properties
# del bottle.name

# Delete an Object

bottle.bottleCalling()

testing = Test()
print(testing)

print("End of practice")
