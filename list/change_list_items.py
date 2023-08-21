fruits = ["Orange", "Banana", "Apple", "Apple", "test", "test"]
fruits[3] = "Grapes"
fruits[4:6] = ["Mango", "Tomato"]
fruits.insert(1, "Cherry")
# ['Orange', 'Cherry', 'Banana', 'Apple', 'Grapes', 'Mango', 'Tomato']
print(fruits)
fruits[1:3] = ["Peach"]
print(fruits)  # ['Orange', 'Peach', 'Grapes', 'Mango', 'Tomato']
