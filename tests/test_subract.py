import unittest

from main import subtract


class TestSubtractFunctions(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(5, subtract(10, 5))


if __name__ == "__main__":
    unittest.main()