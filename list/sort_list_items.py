fruits = ["orange", "banana", "grapes"]
numbers = [1, 32, 442, 0, 2, -1, 42]
thislist = [100, 50, 65, 82, 23]

numbers.sort()
numbers.sort(reverse=True)
fruits.sort()
fruits.sort(reverse=True)
# Use this if you to make all text small to make sorted correctly
thislist.sort(key=str.lower)

thislist.reverse()


def myfunc(n):
    return abs(n - 50)


thislist.sort(key=myfunc)
print(thislist)

print(fruits)
print(numbers)
