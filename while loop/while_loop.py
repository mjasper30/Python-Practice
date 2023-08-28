i = 0

while i < 6:
    print("Hello World " + str(i))
    if i == 3:
        break
    i += 1

j = 0
while j < 5:
    j += 1
    if j == 3:
        continue
    print("Header" + str(j))
else:
    print("End of the loop")
