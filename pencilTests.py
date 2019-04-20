import unittest
from pencil import Pencil

class PencilTester(unittest.TestCase):
    
    def setUp(self):
        """Runs once per test to define a fresh object."""
        self.my_pencil = Pencil(50, 5, 10)
    
    def tearDown(self):
        """Runs once per test to delete object"""
        del(self.my_pencil)

    def test_if_pencil_writes_a_word_it_is_outputted(self):
        self.assertEqual(self.my_pencil.write("hello"), "hello")

    def test_if_pencil_writes_another_word_it_is_appended_to_the_sheet(self):
        self.my_pencil.write("hello")
        self.assertEqual(self.my_pencil.write(" world!"), "hello world!")

    def test_if_pencil_writes_too_many_characters_its_durability_goes_to_zero(self):
        self.my_pencil.set_tip_durability(4)
        self.my_pencil.write("hello")
        self.assertEqual(self.my_pencil.get_tip_durability(), 0)

    def test_if_pencil_durability_is_zero_it_no_longer_writes_characters(self):
        self.my_pencil.set_tip_durability(4)
        self.assertEqual(self.my_pencil.write("hello"), "hell")

    def test_if_durability_is_not_affected_by_whitespace(self):
        self.my_pencil.set_tip_durability(4)
        self.assertEqual(self.my_pencil.write("ab cd"), "ab cd")

    def test_if_durability_is_affected_by_case_of_characters(self):
        self.my_pencil.set_tip_durability(4)
        self.assertEqual(self.my_pencil.write("Hello"), "Hel")

    def test_if_pencil_is_sharpened_its_durability_is_reset(self):
        self.my_pencil.set_tip_durability(4)
        self.my_pencil.write("Hello")
        self.assertEqual(self.my_pencil.get_tip_durability(), 0)
        self.my_pencil.sharpen()
        self.assertEqual(self.my_pencil.get_tip_durability(), 4)

    def test_if_pencil_is_sharpened_its_length_is_reduced(self):
        self.my_pencil.set_length(2)
        self.my_pencil.sharpen()
        self.assertEqual(self.my_pencil.get_length(), 1)

    def test_if_pencil_length_is_zero_it_cannot_be_sharpened_anymore(self):
        self.my_pencil.set_length(0)
        self.my_pencil.set_tip_durability(0)
        self.assertEqual(self.my_pencil.sharpen(), False)
        self.assertEqual(self.my_pencil.get_tip_durability(), 0)

    def test_if_word_is_erased_its_replaced_with_spaces(self):
        self.my_pencil.write("hello world!")
        self.assertEqual(self.my_pencil.erase("world"), "hello      !")

    def test_if_more_than_one_of_same_word_the_last_occurrence_of_word_is_erased(self):
        self.my_pencil.write("up up down down left right left right")
        self.assertEqual(self.my_pencil.erase("left"), "up up down down left right      right")

    def test_if_erasing_reduces_eraser_durability(self):
        self.my_pencil.write("hello world!")
        self.my_pencil.set_eraser_durability(5)
        self.my_pencil.erase("world")
        self.assertEqual(self.my_pencil.get_eraser_durability(), 0)

    def test_that_whitespace_does_not_degrade_eraser(self):
        self.my_pencil.write("hello world!")
        self.my_pencil.set_eraser_durability(6)
        self.my_pencil.erase(" world")
        self.assertEqual(self.my_pencil.get_eraser_durability(), 1)

    def test_if_eraser_durability_reaches_zero_then_it_stops_erasing_from_the_right(self):
        self.my_pencil.write("shinedown")
        self.my_pencil.set_eraser_durability(5)
        self.assertEqual(self.my_pencil.erase("shinedown"), "shin     ")

    def test_if_a_word_is_erased_you_can_edit_to_write_over_the_whitespace(self):
        self.my_pencil.write("your mother was a hamster")
        self.my_pencil.erase("mother")
        self.assertEqual(self.my_pencil.rewrite("mom"), "your mom    was a hamster")

if __name__ == "__main__":
    unittest.main(verbosity=2)