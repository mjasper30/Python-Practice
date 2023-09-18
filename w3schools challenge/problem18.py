def reverse_string(s):
    reverse_string = ''

    index = len(s)

    while index > 0:
        reverse_string += s[index - 1]
        index -= 1

    return reverse_string


print(reverse_string("Just reverse my string"))
