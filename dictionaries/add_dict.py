student = {
    "name": "Jasper",
    "course": "BSCS",
    "age": 21,
    "isEnrolled": True,
    "favColor": ["black", "white", "blue", "gray"]
}

# First way to add key and value in dict
student["pet"] = "cat"

# Second way
student.update({"gender": "male"})

print(student)
