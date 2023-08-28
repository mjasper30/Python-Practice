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
