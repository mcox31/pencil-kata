import unittest
from pencil import Pencil

class PencilTester(unittest.TestCase):
    def test_if_pencil_writes_a_word_it_is_outputted(self):
        my_pencil = Pencil()
        self.assertEqual(my_pencil.write("hello"), "hello")

if __name__ == "__main__":
    unittest.main()