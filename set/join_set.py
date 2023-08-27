set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = {"a", "b", "c"}
set4 = {1, 2, 3}

x = {"Jasper", "Ira", "Poppy"}
y = {"Ralph", "Zoe", "Zed", "Ira", "Luffy", "Jasper"}

set_union = set1.union(set2)
set3.update(set4)

x.intersection_update(y)
z = x.intersection(y)
print(x)
print(z)

print("--------------")

# x.symmetric_difference_update(y)
z = x.symmetric_difference(y)
print(x)
print(z)

print(set_union)
print(set3)
