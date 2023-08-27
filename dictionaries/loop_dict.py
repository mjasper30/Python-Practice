student = {
    "name": "Jasper",
    "course": "BSCS",
    "age": 21,
    "isEnrolled": True,
    "favColor": ["black", "white", "blue", "gray"]
}

# print all the keys
for x in student:
    print(x)

print("-------------")

# pritn all the values
for y in student:
    print(student[y])

print("-------------")

# print all the values in othey way
for z in student.values():
    print(z)

print("-------------")

# print all the keys in the variable
for key in student.keys():
    print(key)

# print all the items in the dictionary
for item in student.items():
    print(item)

"""
OUTPUT

name
course
age
isEnrolled
favColor
('name', 'Jasper')
('course', 'BSCS')
('age', 21)
('isEnrolled', True)
('favColor', ['black', 'white', 'blue', 'gray'])
"""
