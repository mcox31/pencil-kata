import unittest
from pencil import Pencil

class PencilTester(unittest.TestCase):
    
    def setUp(self):
        """Runs once per test to define a fresh object."""
        self.my_pencil = Pencil(15, 5)
    
    def tearDown(self):
        """Runs once per test to delete object"""
        del(self.my_pencil)

    def test_if_pencil_writes_a_word_it_is_outputted(self):
        self.assertEqual(self.my_pencil.write("hello"), "hello")

    def test_if_pencil_writes_another_word_it_is_appended_to_the_sheet(self):
        self.my_pencil.write("hello")
        self.assertEqual(self.my_pencil.write(" world!"), "hello world!")

    def test_if_pencil_writes_too_many_characters_its_durability_goes_to_zero(self):
        self.my_pencil.set_durability(4)
        self.my_pencil.write("hello")
        self.assertEqual(self.my_pencil.get_durability(), 0)

    def test_if_pencil_durability_is_zero_it_no_longer_writes_characters(self):
        self.my_pencil.set_durability(4)
        self.assertEqual(self.my_pencil.write("hello"), "hell")

    def test_if_durability_is_not_affected_by_whitespace(self):
        self.my_pencil.set_durability(4)
        self.assertEqual(self.my_pencil.write("ab cd"), "ab cd")

    def test_if_durability_is_affected_by_case_of_characters(self):
        self.my_pencil.set_durability(4)
        self.assertEqual(self.my_pencil.write("Hello"), "Hel")

    def test_if_pencil_is_sharpened_its_durability_is_reset(self):
        self.my_pencil.set_durability(4)
        self.my_pencil.write("Hello")
        self.assertEqual(self.my_pencil.get_durability(), 0)
        self.my_pencil.sharpen()
        self.assertEqual(self.my_pencil.get_durability(), 4)

    def test_if_pencil_is_sharpened_its_length_is_reduced(self):
        self.my_pencil.set_length(2)
        self.my_pencil.sharpen()
        self.assertEqual(self.my_pencil.get_length(), 1)

    def test_if_pencil_length_is_zero_it_cannot_be_sharpened_anymore(self):
        self.my_pencil.set_length(0)
        self.my_pencil.set_durability(0)
        self.assertEqual(self.my_pencil.sharpen(), False)
        self.assertEqual(self.my_pencil.get_durability(), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)