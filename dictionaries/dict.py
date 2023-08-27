student = {
    "name": "Jasper",
    "course": "BSCS",
    "age": 21,
    "isEnrolled": True,
    "favColor": ["black", "white", "blue", "gray"]
}

# if the key exist in dictionary it will overwrite the last value
student_not_allow_duplicate = {
    "name": "Jasper",
    "course": "BSCS",
    "course": "BSIT",
    "age": 21
}

dict_constructor = dict(name="Jasper", age=21, course="BSCS")

print(student)
print(student_not_allow_duplicate)
print(dict_constructor)
print(type(student))
print(len(student))
print(
    "Hello my name is " + student["name"] + " I am " + str(student["age"]) + " years old and my course is " + student["course"])
