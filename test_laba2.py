import unittest
from test_proverka import UtilityFunctions

class TestUtilityFunctions(unittest.TestCase):

    def test_sort_array(self):
        arr = [2, 3, 4, 2, 2, 11, 12]
        sorted_arr = UtilityFunctions.sort_array(arr)
        self.assertEqual(sorted_arr, [2, 2, 2, 3, 4, 11, 12])

    def test_is_palindrome(self):
        self.assertTrue(UtilityFunctions.is_palindrome("racecar"))
        self.assertFalse(UtilityFunctions.is_palindrome("hello"))

    def test_factorial(self):
        self.assertEqual(UtilityFunctions.factorial(5), 120)
        self.assertEqual(UtilityFunctions.factorial(0), 1)
        with self.assertRaises(ValueError):
            UtilityFunctions.factorial(-1)
    
    def test_calculate(self):
        self.assertEqual(UtilityFunctions.calculate(5), 5)
        self.assertEqual(UtilityFunctions.calculate(1), 1)
        with self.assertRaises(ValueError):
            UtilityFunctions.calculate(0)
    
    def test_power(self):
        self.assertEqual(UtilityFunctions.power(2, 3), 8.0)
        self.assertEqual(UtilityFunctions.power(3.5, 2), 12.25)
        with self.assertRaises(ValueError):
            UtilityFunctions.power("invalid", 2)
    
    def test_is_prime(self):
        self.assertEqual(UtilityFunctions.is_prime(7), "Простое число")
        self.assertEqual(UtilityFunctions.is_prime(4), "Не простое число")
        with self.assertRaises(ValueError):
            UtilityFunctions.is_prime("invalid")

if __name__ == '__main__':
    unittest.main()