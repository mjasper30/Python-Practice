fruits = ["Orange", "Banana", "Apple", "Apple", 1, True]

fruits.remove(1)  # value
fruits.pop(0)  # index
fruits.pop()  # if you dont specify it will remove the last item

del fruits[0]
del fruits  # delete the entire list meaning fruits not exist anymore

fruits = ["Orange", "Banana", "Apple", "Apple", 1, True]
fruits.clear()

print(bool(fruits))
