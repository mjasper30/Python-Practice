import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("ai", txt)
z = re.split("\s", txt)
a = re.sub("\s", "9", txt)
print(y)
print(z)
print(a)

if x:
    print("YES! We have a match!")
else:
    print("No match")
