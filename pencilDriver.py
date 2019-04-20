from pencil import Pencil
from pencilTests import PencilTester
import unittest

# Driver class. Runs through command line.
# Can execute unit tests and also use the pencil class.

print("Welcome to the pencil driver program. Please enter a number to make a"
      " selection.")

while True:
    print("1. Create a pencil.")
    print("2. Edit your pencil.")
    print("3. View current pencil stats.")
    print("4. Write with your pencil.")
    print("5. Sharpen your pencil.")
    print("6. Erase Words.")
    print("7. Rewrite erased words.")
    print("8. Run unit tests.")
    print("9. Quit driver program")

    selection = int(input("Enter selection number: "))

    print(f"Your selection is: {selection}")

    # choice handler
    if selection == 1:
        create_new_pencil()
        continue
    elif selection == 2:
        edit_pencil()
        continue

    elif selection == 3:
        view_pencil_stats()
        continue

    elif selection == 4:
        write_with_pencil()
        continue

    elif selection == 5:
        sharpen_pencil()
        continue

    elif selection == 6:
        erase_words()
        continue

    elif selection == 7:
        rewrite_words()
        continue

    elif selection == 8:
        print_unit_tests()
        continue

    elif selection == 9:
        break

    else:
        print("Error: incorrect input. Please try again.")


def create_new_pencil():
    pass


def edit_pencil():
    pass

def view_pencil_stats():
    pass

def write_with_pencil():
    pass


def sharpen_pencil():
    pass


def erase_words():
    pass


def rewrite_words():
    pass


def print_unit_tests():
    pass
