txt = 'We are the so-called \'Vikings\' from the north. Just add backslash here \'\\\'\n go to new line hello i am a new line just add tab here \t bleh\b bleh.'
secretCode = "\110\145\154\154\157"  # octal value in ASCII table

print(txt)
print(secretCode)  # output: Hello
print("\112\141\163\160\145\162")  # output: Jasper - in octal value
print("\x4A\x61\x73\x70\x65\x72")  # output: Jasper - in hex value
