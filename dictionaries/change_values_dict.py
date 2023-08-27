student = {
    "name": "Jasper",
    "course": "BSCS",
    "age": 21,
    "isEnrolled": True,
    "favColor": ["black", "white", "blue", "gray"]
}

student["age"] = 22
student.update({"course": "BSEMC"})

print(student)
