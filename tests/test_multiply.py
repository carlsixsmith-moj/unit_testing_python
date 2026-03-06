import unittest

from main import multiply


class TestMultiplyFunctions(unittest.TestCase):
    def test_multiply_two_positive_numbers(self):
        self.assertEqual(10, multiply(5,2))
        self.assertEqual(100, multiply(10,10))

    def test_mutilply_two_negative_numbers(self):
        self.assertEqual(10, multiply(-5,-2))
        self.assertEqual(100, multiply(-10, -10))
        
    def test_multiply_positive_with_negative(self):
        self.assertEqual(-10, multiply(5, -2))
        self.assertEqual(-100, multiply(10, -10))

if __name__ == "__main__":
    unittest.main()
