x = {"Jasper", "Ira", "Poppy"}
y = {"Ralph", "Zoe", "Zed", "Ira", "Luffy", "Jasper", "Poppy"}

z = x.isdisjoint(y)
a = x.issubset(y)
b = y.issuperset(x)

print(z)
print(a)
print(b)
