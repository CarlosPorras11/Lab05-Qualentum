import unittest
from plus import plus

class TestPlus(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(plus(1,8),8)
        self.assertEqual(plus(7,8),56)
        self.assertEqual(plus(20,-8),-160)

if __name__ == "__main__":

    unittest.main()