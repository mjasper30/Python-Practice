thisset = {"apple", "banana", "cherry"}

# remove value based on the parameter if its not found it gets error
thisset.remove("apple")

# remove value based on the parameter even though its not found it doesnt get any error
thisset.discard("bananaa")

# remove the last value of the set
thisset.pop()

# remove the values of the set
thisset.clear()

# remove the set entirely to the code
del thisset

print(thisset)
