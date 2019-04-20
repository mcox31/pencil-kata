import unittest
from pencil import Pencil

class PencilTester(unittest.TestCase):
    def test_if_pencil_writes_a_word_it_is_outputted(self):
        my_pencil = Pencil(10)
        self.assertEqual(my_pencil.write("hello"), "hello")

    def test_if_pencil_writes_another_word_it_is_appended_to_the_sheet(self):
        my_pencil = Pencil(10)
        my_pencil.write("hello")
        self.assertEqual(my_pencil.write(" world!"), "hello world!")

    def test_if_pencil_writes_too_many_characters_its_durability_goes_to_zero(self):
        my_pencil = Pencil(4)
        my_pencil.write("hello")
        self.assertEqual(my_pencil.check_durability(), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)