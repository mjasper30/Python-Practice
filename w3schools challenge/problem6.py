"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

n = str(input("Sample value of n is "))

print(f"Expected Result : {int(n) + int(str(n + n)) + int(str(n + n + n))}")
