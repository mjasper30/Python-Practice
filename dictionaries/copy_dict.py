student = {
    "name": "Jasper",
    "course": "BSCS",
    "age": 21,
    "isEnrolled": True,
    "favColor": ["black", "white", "blue", "gray"]
}

# One Way
copy_student = student.copy()

# Other Way
copy_student2 = dict(student)

print(copy_student)
print(copy_student2)
