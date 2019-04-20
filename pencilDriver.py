from pencil import Pencil
from pencilTests import PencilTester
import pencilDriverFunctions as pf
import unittest


# Driver class. Runs through command line.
# Can execute unit tests and also use the pencil class.

print("Welcome to the pencil driver program. Please enter a number to make a"
      " selection.")

while True:
    print("1. Create a pencil.")
    print("2. Edit your pencil.")
    print("3. View current pencil stats and paper.")
    print("4. Write with your pencil.")
    print("5. Sharpen your pencil.")
    print("6. Erase Words.")
    print("7. Write over erased words.")
    print("8. Run unit tests. (Quits program)")
    print("9. Quit driver program")

    selection = pf.get_selection("Enter your selection: ")

    # choice handler
    if selection == 1:
        pf.create_new_pencil()
        continue
    elif selection == 2:
        pf.edit_pencil()
        continue
    elif selection == 3:
        pf.view_pencil_stats_and_paper()
        continue
    elif selection == 4:
        pf.write_with_pencil()
        continue
    elif selection == 5:
        pf.sharpen_pencil()
        continue
    elif selection == 6:
        pf.erase_words()
        continue
    elif selection == 7:
        pf.rewrite_words()
        continue
    elif selection == 8:
        pf.print_unit_tests()
        continue
    elif selection == 9:
        print("\nThank you for using the pencil driver program. Goodbye.\n")
        break
    else:
        pf.print_incorrect_selection()
