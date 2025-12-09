from colorama import Fore, Style, Back


def get_size():
    size = int(input("How big do you want your tree? (in feet) "))

    return size


def get_theme():
    color = input("What's your color scheme? (classy, retro, or funky? ")

    return color


def get_fortune(): ...


def print_tree(size, color):
    # Leaves
    for i in range(size):
        print(
            (" " * (size - i)) + (f"{Fore.GREEN}#{Style.RESET_ALL}" * (i + i - 1)),
            end="\n",
        )

    # Trunk
    print(" " * (size - 3) + (f"{Back.RED}     {Style.RESET_ALL}"))


# Main function
# How many feet tall do you want the tree? (Pick a number betweeen 5 and 10 feet)

# Include a holiday fortune? OR Write custom message?


def main():
    size = get_size()

    color = get_theme()

    print_tree(size, color)


main()
