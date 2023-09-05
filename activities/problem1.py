#! Leason 3 Activity Cabfit/Macaraeg // OK

"""
Sample data set:
55 57 55 60 51 90 100 99 85 51 60 57 90 55
Test Case #1
Test Score Count
51 2
55 3
57 2
60 2
85 1
90 2
99 1
100 1
"""

numbers = str(input("Sample data set: "))
list = numbers.split(" ")


for i in range(0, len(list)):
    list[i] = int(list[i])

list.sort()
convertedSet = sorted(set(list))

print("Test Score\tCount")

for test_scores in convertedSet:
    print(str(test_scores) + "\t\t " + str(list.count(test_scores)))