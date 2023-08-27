"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

input = input(str("Sample filename: "))

array = input.split('.')

print(array[-1])
