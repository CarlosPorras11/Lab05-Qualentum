import unittest
from sum import sum

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum(1, 8), 9)
        self.assertEqual(sum(-7, 8), 1)
        self.assertEqual(sum(-1,-5), -6)


if __name__ == "__main__":

    unittest.main()
