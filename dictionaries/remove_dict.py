student = {
    "name": "Jasper",
    "course": "BSCS",
    "age": 21,
    "isEnrolled": True,
    "favColor": ["black", "white", "blue", "gray"]
}

# remove item based on the key
student.pop("course")

# remove the last item in dictionary
student.popitem()

# clear all the key and value pairs in the dictionary
student.clear()

# delete the item based on the key
del student["age"]

# delete the entire dictionary
del student

print(student)
