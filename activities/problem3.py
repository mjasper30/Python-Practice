#! Leason 3 Activity Cabfit/Macaraeg // OK

list = []
while True:
    word = input("Enter a word: ")
    conti = input("Do you want to try again? Y/N : ")
    if conti == 'Y' or conti == 'y':
        list.append(word)
    elif conti == 'N' or conti == 'n':
        list.append(word)
        print("Total number of Words: " + str(len(list)))
        for x in list:
            print(x)
        break
    else:
        print("Invalid Input")