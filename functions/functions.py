def printHelloWorld():
    print("Hello World")

# pass parameters in function
# value name is what called parameters


def myName(name):
    print("Hello my name is " + name)


printHelloWorld()
myName("Jasper")  # the value "Jasper" is called arguments

# Arbritary Arguments - *args


def threeFavColor(*color):
    print("My three favorite colors " +
          color[0] + " " + color[1] + " " + color[2])


threeFavColor("Black", "Blue", "White")

# Keyword Arguments


def myStudents(student3, student2, student1):
    print("These are my three students ", student1, student2, student3)


myStudents(student1="Jasper", student2="Ira", student3="Poppy")

# Arbitrary Keyword Arguments - **kwargs


def myFruits(**fruit):
    print("My fruits are ", fruit["red"], fruit["green"], fruit["orange"])


myFruits(red="strawberry", green="guava", orange="orange")

# Set default value


def sayHello(sayIt="Hello"):
    print("Say", sayIt)


sayHello()
sayHello("Hi")

# Passing List as an argument


def showAllList(list):
    for x in list:
        print(x)


myList = ["List 1", "List 2", "List 3"]

showAllList(myList)

# function that returns a value


def showSum(x, y):
    return x + y


print(showSum(2, 2))


def nothingJustPass():
    pass


nothingJustPass()

# Recursion


def tri_recursion(k):
    if (k > 0):  # 6 > 0
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
