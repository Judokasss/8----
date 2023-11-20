import unittest
from проверка import UtilityFunctions

class TestUtilityFunctions(unittest.TestCase):
    # СОРТИРОВКА МАССИВА
    def test_sort_array(self):
        arr = [2, 3, 4, 2, 2, 11, 12]
        sorted_arr = UtilityFunctions.sort_array(arr)
        self.assertEqual(sorted_arr, [2, 2, 2, 3, 4, 11, 12])
    
    def test_sort_array_empty(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.sort_array([])

    def test_sort_array_invalid_input(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.sort_array(["a", "b", "c"])

    # ПАЛИНДРОМ
    def test_is_palindrome(self):
        self.assertTrue(UtilityFunctions.is_palindrome("racecar"))
        self.assertFalse(UtilityFunctions.is_palindrome("hello"))
    
    def test_is_palindrome_empty_string(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.is_palindrome("")

    def test_is_palindrome_whitespace(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.is_palindrome("  ")

    def test_is_palindrome_invalid_characters(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.is_palindrome("//??")
            
    # ФАКТОРИАЛ
    def test_factorial(self):
        self.assertEqual(UtilityFunctions.factorial(5), 120)
        self.assertEqual(UtilityFunctions.factorial(0), 1)
    
    def test_factorial_negative_integer(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.factorial(-1)

    def test_factorial_invalid_input_string(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.factorial("dsd")

    def test_factorial_invalid_input_float(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.factorial(2.2)

    def test_factorial_empty_string(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.factorial("")

    # ФИБОНАЧЧИ
    def test_calculate(self):
        self.assertEqual(UtilityFunctions.calculate(5), 5)
        self.assertEqual(UtilityFunctions.calculate(1), 1)
    
    def test_calculate_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.calculate(0)

    def test_calculate_invalid_input_empty_string(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.calculate("")

    def test_calculate_invalid_input_float(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.calculate(2.3)

    def test_calculate_invalid_input_negative_integer(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.calculate(-12)

    def test_calculate_invalid_input_string(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.calculate("dsd")
    
    # ВОЗВЕДЕНИЕ В СТЕПЕНЬ
    def test_power_integer_base_and_exponent(self):
        self.assertEqual(UtilityFunctions.power(2, 3), 8.0)

    def test_power_float_base_and_integer_exponent(self):
        self.assertEqual(UtilityFunctions.power(3.5, 2), 12.25)

    def test_power_float_base_and_float_exponent(self):
        self.assertEqual(UtilityFunctions.power(2.2, 2.2), 5.67)

    def test_power_invalid_base(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.power("invalid", 2.3)

    def test_power_invalid_base_and_exponent(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.power("invalid", "Hello Kitty")

    # ПРОВЕРКА НА ПРОСТО ЧИСЛО        
    def test_is_prime_prime_number(self):
        self.assertEqual(UtilityFunctions.is_prime(7), "Простое число")

    def test_is_prime_non_prime_number(self):
        self.assertEqual(UtilityFunctions.is_prime(4), "Не простое число")

    def test_is_prime_invalid_input_string(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.is_prime("invalid")

    def test_is_prime_invalid_input_float(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.is_prime(21.2)

    def test_is_prime_invalid_input_empty_string(self):
        with self.assertRaises(ValueError):
            UtilityFunctions.is_prime(" ")

if __name__ == '__main__':
    unittest.main()