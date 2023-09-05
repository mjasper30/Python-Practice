#! Leason 3 Activity Cabfit/Macaraeg // OK

"""
Test Case 1:
Record Keeping App
a. Add Data
b. Delete Data
c. End
Enter your choice: a
=======ADD NEW RECORD==========
Enter Key: go
Enter Value: jake
=======DISPLAY RECORD==========
go: jake
=======END OF RECORD==========
Record Keeping App
a. Add Data
b. Delete Data
c. End
Enter your choice: a
=======ADD NEW RECORD==========
Enter Key: santos
Enter Value: joel
=======DISPLAY RECORD==========
go: jake
santos: joel
=======END OF RECORD==========
Record Keeping App
a. Add Data
b. Delete Data
c. End
Enter your choice: b
=======DELETE RECORD==========
Enter Key: santos
=======DISPLAY RECORD==========
go: jake
=======END OF RECORD==========
Record Keeping App
a. Add Data
b. Delete Data
c. End
Enter your choice: c
Thank you!
"""

menu = """
Record Keeping App
a. Add Data
b. Delete Data
c. End
"""

dict = {}

while True:
    print(str(menu))
    user = input("Enter your choice: ")

    if user == "a":
        print("=======ADD NEW RECORD==========")
        key = input("Enter Key: ")
        val = input("Enter Value: ")
        dict[key] = val
        print("=======DISPLAY RECORD==========")
        for x in dict:
            print(f"{x} : {dict[x]}")
    elif user == "b":
        print("=======DELETE RECORD==========")
        key = input("Enter Key: ")
        
        dict.pop(key)
        print("=======DISPLAY RECORD==========")
        for x in dict:
            print(f"{x} : {dict[x]}")
            
    elif user == "c":
        print("Thank you!")
        break
    else:
        print("Invalid Input")