import unittest

from main import add

class TestMainFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
       self.assertEqual(4, add(2,2))
       self.assertEqual(100, add(70,30))
    
    def test_add_negative_numbers(self):
        self.assertEqual(-2, add(-1, -1))
        self.assertEqual(-100, add(-70, -30))
    
    def test_add_positive_to_negative(self):
        self.assertEqual(-10, add(10, -20))
        self.assertEqual(-100, add(100, -200))

if __name__ == "__main__":
    unittest.main()