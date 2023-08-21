fruits = ["Orange", "Banana", "Apple"]
anotherFruits = ["Cherry", "Mango"]
tuples_items = ("Item 1", "Item 2")

if "orange" in fruits:
    fruits.append("Grapes")  # add item at the end of the list
else:
    fruits.insert(0, "Walang ganon")

fruits.extend(tuples_items)  # you can extend any iteratable objects
print(fruits)
