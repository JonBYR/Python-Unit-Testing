import unittest
from calculator import add, is_prime
class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)
    def test_add_positive_negative_numbers(self):
        self.assertEqual(add(2,-3), -1)
    def test_true(self):
        self.assertTrue(is_prime(2))
    def test_false(self):
        self.assertFalse(is_prime(4))
    def test_exception(self):
        self.assertRaises(TypeError, is_prime, 3.5)
if __name__ == "__main__":
    unittest.main()