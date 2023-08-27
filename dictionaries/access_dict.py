student = {
    "name": "Jasper",
    "course": "BSCS",
    "age": 21,
    "isEnrolled": True,
    "favColor": ["black", "white", "blue", "gray"]
}

# to more keys in dict
student["pet"] = "cat"

# get the value and store it to a variable
x = student["favColor"][0]
y = student.get("course")

# store value of keys in variable
getKeys = student.keys()

# store value of values in variable
getValues = student.values()

# store key:value in variable
getItems = student.items()

print(x)
print(y)

# print the keys
print(getKeys)

# print the values
print(getValues)

# print the key:value
print(getItems)

# to check if there is existing key
if "age" in student:
    print("There is key named age in the dictionary")
else:
    print("The age key is not exist")
