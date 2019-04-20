from pencil import Pencil
import pencilTests as pt
import unittest

my_pencil = Pencil(1,1,1)

def get_selection(message):
    selection = int(input(message))
    return selection

def create_new_pencil():
    tip_durability = get_selection("Enter tip durability: ")
    length = get_selection("Enter pencil length: ")
    eraser_durability = get_selection("Enter eraser durability: ")
    my_pencil.set_tip_durability(tip_durability)
    my_pencil.set_length(length)
    my_pencil.set_eraser_durability(eraser_durability)
    print_divider()
    print("\nCreated new pencil with the following stats:")
    my_pencil.print_pencil_stats()
    print_divider()

def edit_pencil():
    print_divider()
    print("1. Change tip durability.")
    print("2. Change length.")
    print("3. Change eraser durability.")

    selection = get_selection("Enter your selection: ")
    
    if selection == 1:
        my_pencil.set_tip_durability(get_selection("Enter new tip durability: "))
    elif selection == 2:
        my_pencil.set_length(get_selection("Enter new length: "))
    elif selection == 3:
        my_pencil.set_eraser_durability(get_selection("Enter new eraser durability: "))
    else:
        print_incorrect_selection()
    print_stats_and_paper()

def view_pencil_stats_and_paper():
    print_divider()
    print_stats_and_paper()

def write_with_pencil():
    print_divider()
    try:
        my_pencil.write(input("Enter what to write: "))
    except:
        print_incorrect_selection()
    print_stats_and_paper()

def sharpen_pencil():
    print_divider()
    my_pencil.sharpen()
    print_stats_and_paper()

def erase_words():
    print_divider()
    try:
        my_pencil.erase(input("Enter what to erase: "))
    except:
        print_incorrect_selection()
    print_stats_and_paper()

def rewrite_words():
    print_divider()
    try:
        my_pencil.rewrite(get_selection("Enter index of erased word to replace: "), input("Enter words to write: "))
    except:
        print_incorrect_selection()
    print_stats_and_paper()

def print_unit_tests():
    print_divider()
    print("Running unit tests.\n")
    pt.run_unit_tests()

def print_divider():
    divider = ""
    for x in range(50):
        divider = divider + "-"
    print("\n" + divider + "\n")

def print_incorrect_selection():
    print("Error: incorrect input. Please try again.")

def print_stats_and_paper():
    print_divider()
    my_pencil.print_pencil_stats()
    my_pencil.print_sheet_of_paper()
    print_divider()