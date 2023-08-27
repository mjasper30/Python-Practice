"""
Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""


def sum(x, y, z):
    if x == y or y == z or z == x:
        return print(0)
    else:
        return print(x + y + z)


sum(5, 5, 5)
sum(5, 1, 2)
