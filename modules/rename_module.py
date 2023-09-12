import mymodule as custommodule
import platform

a = custommodule.person1["age"]
x = platform.system()

mydir = dir(platform)

print(a)
print(x)
print(mydir)
