list1 = ["Apple", "Banana", "Orange"]
list2 = ["Mango", "Cherry"]

combine_list = list1 + list2

# Another way of join list by using append and loop

for list in list1:
    list2.append(list)

# or you can use the extend method

list1.extend(list2)

print(list1)
print(list2)
print(combine_list)
