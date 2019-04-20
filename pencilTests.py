import unittest
from pencil import Pencil

class PencilTester(unittest.TestCase):
    
    def setUp(self):
        """Runs once per test to define a fresh object."""
        self.my_pencil = Pencil(10)
    
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
        self.assertEqual(self.my_pencil.check_durability(), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)