from colorama import Fore, Style, Back

from random import randint

fortunes = (
    "Congrats! You will not be getting socks this year",
    "You'll be getting a white Christmas this year",
    "You're going to get the best white elephant gift at the party",
    "New Year's will be more exciting than the holidays this year",
    "Someone is going to be elated with the gift you give them this year",
    "The holidays this year will be one of the most memorable of all time",
    "You won't need to drive to see family this year",
    "Your tree will be the envy of all of your friends and family",
    "You're going to be overbooked with holiday parties, with how popular you are",
    "You're going to see Santa, for real. Yes, he's been real this whole time!",
)


def get_size():
    size = int(input("How big do you want your tree? (in feet) "))

    return size


def get_fortune(fortunes):
    i = randint(0, len(fortunes) - 1)

    return fortunes[i]


def print_tree(size):
    # Star
    print((" " * (size - 2)) + (f"{Fore.YELLOW} * "), end="")

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
    print("\n")

    size = get_size()

    print("\n")

    print(f"{Back.RED}{Fore.WHITE}*{Style.RESET_ALL}" * 100)

    print("\n", end="")


    print_tree(size)

    print("\n")

    fortune = get_fortune(fortunes)

    print(f"{Fore.GREEN}{fortune}")


    print("\n")

    print(f"{Back.RED}{Fore.WHITE}*{Style.RESET_ALL}" * 100)

    print("\n", end="")


main()
