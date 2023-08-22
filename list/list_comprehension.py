students = ["Jasper", "Ira", "Patrick", "Daneris", "John Kenneth"]
contains_e = []

for student in students:
    if "e" in student:
        contains_e.append(student)

# Single line of code
# Syntax = newlist = [expression for item in iterable if condition == True]
pro_contains_e = [student for student in students if "e" in student]
pro_contains_Jasper = [student for student in students if "Jasper" != student]
newlist = [x for x in students]
newlist1 = [x for x in range(1, 10 + 1)]
newlist2 = [x for x in range(1, 10) if x < 5]
listToUpper = [student.upper() for student in students]
setAllToHello = ["Hello" for student in students]
# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
newlist3 = [x if x != "Jasper" else "orange" for x in students]

print(contains_e)
print(pro_contains_e)
print(pro_contains_Jasper)
print(newlist)
print(newlist1)
print(newlist2)
print(listToUpper)
print(setAllToHello)
print(newlist3)
