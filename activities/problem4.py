#! Leason 3 Activity Cabfit/Macaraeg // OK

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

for count in sentence:
    if count.isdigit():
        digits += 1
    elif count.isalpha():
        letters += 1
    else:
        pass

print(f"Letters: {letters}")
print(f"Digits: {digits}")