fruits = ("Orange", "Apple", "Grapes", "Mango", "Cherry")
deletion = ("Orange", "Apple", "Grapes", "Mango", "Cherry")

convert_list = list(fruits)
convert_list[0] = "Banana"
convert_list.remove("Grapes")
convert_tuple = tuple(convert_list)

fruits += ("Papaya",)

del deletion

print(convert_list)
print(convert_tuple)
print(fruits)
print(deletion)  # returns error because this is not exist
