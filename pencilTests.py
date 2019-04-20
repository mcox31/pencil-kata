import unittest
from pencil import Pencil

class PencilTester(unittest.TestCase):
    def test_if_pencil_writes_a_word_it_is_outputted(self):
        my_pencil = Pencil()
        self.assertEqual(my_pencil.write("hello"), "hello")

    def test_if_pencil_writes_another_word_it_is_appended_to_the_sheet(self):
        my_pencil = Pencil()
        my_pencil.write("hello")
        self.assertEqual(my_pencil.write(" world!"), "hello world!")

if __name__ == "__main__":
    unittest.main()