"""
Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

diff = color_list_1.difference(color_list_2)

# sym_diff = color_list_1.symmetric_difference(color_list_2)
# intersec = color_list_1.intersection(color_list_2)
# unio = color_list_1.union(color_list_2)

print(diff)
# print(sym_diff)
# print(intersec)
# print(unio)
