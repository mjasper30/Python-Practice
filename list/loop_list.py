fruits = ["Orange", "Banana", "Apple", "Cherry", "Mango"]

for fruit in fruits:
    print(fruit)

print("----------------")

for i in range(1, 10):
    print("Index number:", i)

print("----------------")

i = 0
while (i < len(fruit)):
    print(fruits[i])
    i = i + 1

print("----------------")

[print(x) for x in fruits]

print("----------------")

for fruit in range(1, 3):
    print(fruits[fruit])

print("----------------")

j = 1

while (j < 3):
    print(fruits[j])
    j += 1

print("----------------")

[print(fruits[fruit]) for fruit in range(1, 3)]
