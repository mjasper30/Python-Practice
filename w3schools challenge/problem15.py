# Chrismas Tree

def print_pattern(height):
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    print(" " * (height - 1) + "|||")


height = 7  # You can adjust the height of the pyramid
print_pattern(height)
