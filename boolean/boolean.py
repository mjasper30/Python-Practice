print(1 < 4)
print(1 == 1)

x = 10
y = 51

if x < y:
    print('First Condition satisfy')
else:
    print('Second Condition satisfy')


"""
#ANY OF THESE RETURN FALSE OTHERWISE TRUE
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""


def myFunction():
    return True


print(myFunction())

if myFunction():
    print("True siya")
else:
    print("False")

# to check if the value reflect to the datatype given
x = "200"
print(isinstance(x, int))
