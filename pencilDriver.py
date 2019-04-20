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
    print("3. Write with your pencil.")
    print("4. Sharpen your pencil.")
    print("5. Erase Words.")
    print("6. Rewrite erased words.")
    print("7. Run unit tests.")
    print("8. Quit driver program")

    selection = input("Enter selection number: ")

    #choice handler
    if selection == 1:
        create_new_pencil()
    elif selection == 2:
        edit_pencil()
    elif selection == 3:
        write_with_pencil()
    elif selection == 4:
        sharpen_pencil()
    elif selection == 5:
        erase_words()
    elif selection == 6:
        rewrite_words()
    elif selection == 7:
        print_unit_tests()
    elif selection == 8:
        break
    else:
        print("Error: incorrect input. Please try again.")

def create_new_pencil():
    pass
    
def edit_pencil():
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
    
