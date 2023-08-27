fruits = ("apple", "banana", True, "cherry")

for x in fruits:
    print(type(x))

print("----------------")

for i in range(1, len(fruits), 2):
    print(fruits[i])

print("----------------")

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
