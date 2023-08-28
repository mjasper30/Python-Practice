fruits = ["apple", "banana", "cherry", "mango"]

# loop through a list
for fruit in fruits:
    print(fruit)

print("------------")

# loop through a string
for char in "mango":
    print(char)

print("------------")

# using break statement in for loop
for fruit in fruits:
    print(fruit)
    if fruit == "cherry":
        break
    # print(fruit)

print("------------")

# using continue statement in for loop
for fruit in fruits:
    if fruit == "cherry":
        continue
    print(fruit)

print("------------")

# using range function
# range (start, end, step)
for x in range(2, 10, 2):  # from 0 to 9
    if x == 6:
        break
    print(x)
else:
    print("End of the for loop")

# using nested loops
color = ["red", "blue", "green"]

for row in fruits:
    for col in color:
        print(row, col)

# using pass
for x in [True, False, True]:
    pass
