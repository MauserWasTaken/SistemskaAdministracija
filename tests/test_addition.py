import unittest
from calculator import add

class TestAddition(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)


if __name__ == '__main__':
    unittest.main()

