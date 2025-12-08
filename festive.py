def get_size():
    ...

def get_style():
    ...

def get_theme(): 
    ...

def get_color(): 
    ...

def get_fortune(): 
    ...

def print_tree(size): 
    # Leaves
    for i in range(size):
        print((" " * (size-i)) + ("#" * (i + i-1)), end="\n")

    # Trunk 
    # Workshop this to get this centered 
    print((" " * (size//2 + 2)) + ("|   |"))


# Main function
    # How many feet tall do you want the tree? (Pick a number betweeen 5 and 10 feet)

    # Minimalist or maximalist?

    # What's your color scheme? (classy, retro, funky)

    # Include a holiday fortune? OR Write custom message?

def main():
    print_tree(10)

main()