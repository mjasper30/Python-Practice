"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

input = input(str("Sample data : "))

split_data = input.split(',')
tuple = tuple(split_data)
list = list(split_data)

print(list)
print(tuple)
