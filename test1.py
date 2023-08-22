number = int(input("Enter a number: "))
firstNumber = 0
sum = 0
plusTwo = 2
nextNumbers = ""
nextNumbersDisplay = ""

i = 0
j = 0

if (number < 1 or number > 30):
    print("The integer input is out of range")
else:
    while i <= number:
        firstNumber = number * (number - 1) + 1

        sum += firstNumber

        while j + 1 < number:
            nextNumbers += " + " + str(int(firstNumber + plusTwo))
            nextNumbersDisplay += str(int(firstNumber + plusTwo)) + " "
            j += 1
            plusTwo += 2

        i += 1

    print(f"{number} = {firstNumber}{str(nextNumbers)} = {sum - 1}")
    print(f"Addends: {firstNumber} {str(nextNumbersDisplay)}")
    print(f"Sum of Addends (Cube): {sum - 1}")

# TESTING LOGIC PURPOSES
# {firstNumber + 2} + {firstNumber + 4} + {firstNumber + 6} + {firstNumber + 8}
# [numbers for number in numbers]
#

# x = str(firstNumber) + " + " + str(firstNumber + 2) + " + " + str(firstNumber +
#                                                                   4) + " + " + str(firstNumber + 6) + " + " + str(firstNumber + 8)
