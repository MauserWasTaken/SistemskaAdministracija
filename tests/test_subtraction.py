import unittest
from calculator import subtract

class TestSubtraction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_mixed_numbers(self):
        self.assertEqual(subtract(5, -3), 8)

    def test_zero(self):
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

