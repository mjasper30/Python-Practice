x = 2
y = 2

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("both are equal")

# short hand of if
if x < y:
    print("x is less than y")

# short hand of else if
print("x is less than y") if x < y else print("x is greater than y")

# short hand of if else if and else
print("x is less than y") if x < y else print(
    "x is greater than y") if x > y else print("both are equal")

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

if a > b or a > c:
    print("At least one of the conditions is True")

if not a > b:
    print("a is NOT greater than b")

if b > a:
    pass
