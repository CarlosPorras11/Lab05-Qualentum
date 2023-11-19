import unittest
from substract import substract

class TestSubstract(unittest.TestCase):
    
    def test_substract(self):
        self.assertEqual(substract(3,5), -2)
        self.assertEqual(substract(7, -12), 19)
        self.assertEqual(substract(-1,5), -6)


if __name__ == "__main__":

    unittest.main()
