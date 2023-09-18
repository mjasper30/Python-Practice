def string_test(s):
    d = {"upper_case": 0, "lower_case": 0}

    for char in s:
        if char.isupper():
            d["upper_case"] += 1
        elif char.islower():
            d["lower_case"] += 1
        else:
            pass

    print("Input String : ", s)
    print("Number of Upper Characters: ", d["upper_case"])
    print("Number of Lower Characters: ", d["lower_case"])


string_test("The Quick BRown FOX")
