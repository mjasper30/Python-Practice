"""
Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""

first_number = int(input("First number: "))
second_number = int(input("Second number: "))
third_number = int(input("Third number: "))

if first_number == second_number == third_number:
    sum = first_number + second_number + third_number
    print(sum * 3)
else:
    sum = first_number + second_number + third_number
    print(sum)
