import unittest

from main import divide


class TestDivideFunctions(unittest.TestCase):
    def test_divide_two_positive_numbers(self):
        self.assertEqual(2, divide(10, 5))
        self.assertEqual(0.5, divide(5, 10))

    def test_divide_two_negative_numbers(self):
        self.assertEqual(2, divide(-10, -5))
        self.assertEqual(10, divide(-100, -10))

if __name__ == "__main__":
    unittest.main()
