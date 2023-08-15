# Print with Strings
x = "Just a string"

y = """
Assigning a string to a variable is 
            done with the variable name 
followed 
by an equal sign and the string
"""

print(x)
print(y)

# Print with Arrays
a = "Hello World"
print(a[1])

# loop through string
for x in "banana":
    print(x)

# Check length of string
text = "Hello World"
print(len(text))

# if the text is exist in the text
print("Hello" in text)  # Output: True

if ("Hello" in text):
    print("Hello is exist!")

print("Hello" not in text)

if ("Hello" not in text):
    print("Hello is not exist")
else:
    print("Hello is exist!")
