"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Test Case 1:
Input Sentence: Hello World 12345
LETTERS: 10
DIGITS: 5
Test Case 2:
Input Sentence: The quick brown f0x jumps ove3 7he lazy do9.
LETTERS: 31
DIGITS: 4
"""

sentence = input("Input Sentence: ")
digits = 0
letters = 0
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upperLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for count in sentence:
    if count in numbers:
        digits += 1
    elif count in alphabet or count in upperLetters:
        letters += 1
    else:
        pass

print(f"Letters: {letters}")
print(f"Digits: {digits}")
