import unittest
from div import div

class TestDiv(unittest.TestCase):

    def test_div(self):
        self.assertEqual(div(8,4),2)
        self.assertEqual(div(0,4), None)
        self.assertEqual(div(100,-10),-10)

if __name__ == "__main__":
    unittest.main()