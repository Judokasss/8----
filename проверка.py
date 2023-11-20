# Импортируем библиотеку для работы с ANSI Escape-кодами
from colorama import init, Fore
# Инициализируем библиотеку Colorama
init(autoreset=True)
class UtilityFunctions:
    @staticmethod
    def sort_array(arr: list) -> list:
        # Проверка на пустоту
        if not arr:
            raise ValueError("Нельзя ввести пустоту.")
            raise ValueError("Нельзя ввести пустоту.")
        
        # Проверка на целые числа
        for item in arr:
            if not isinstance(item, int):
                 raise ValueError("Вводите только целые числа.")

        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def is_palindrome(string: str) -> str:
        # Проверка на пустоту
        if not string.strip():
            raise ValueError("Нельзя вводить пустые значения.")
        
        # Проверка на символы и знаки препинания
        if not string.isalpha():
             raise ValueError("Нельзя вводить символы и знаки препинания.")
        
        clean_string = "".join(char.lower() for char in string if char.isalpha())
        if clean_string == clean_string[::-1]:
            return True
        else:
            return False

    @staticmethod
    def factorial(n: int) -> int:
        # Проверка на пустоту
        if n is None:
            raise ValueError("Аргумент не может быть пустым")

        # Проверка на тип аргумента
        if not isinstance(n, int):
             raise ValueError ("Аргумент должен быть целым числом")

        # Проверка на отрицательное значение
        if n < 0:
             raise ValueError ("Факториал определен только для неотрицательных чисел")

        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

    @staticmethod
    def calculate(n:int )-> int:
        if not n:
             raise ValueError ("Нельзя ввести пустоту.")
        if not isinstance(n, int):
             raise ValueError ("Аргумент должен быть целым числом") 
        if n <= 0:
             raise ValueError ("Позиция должна быть положительным целым числом")
        if n == 1 or n == 2:
            return 1
        prev = 1
        curr = 1
        for _ in range(3, n + 1):# используется _ вместо конкретной переменной, потому что на самом деле значение переменной не используется внутри цикла.
            prev, curr = curr, prev + curr     
        return curr

    @staticmethod
    def power(base: float, exponent: float) -> float:
        if not isinstance(base, (float, int)) or not isinstance(exponent, (float, int)):
             raise ValueError("Аргументы должны быть числами")
    
        result = float(base) ** float(exponent)
        return round(result,2)

    @staticmethod
    def is_prime(number):
        if not isinstance(number, int):
             raise ValueError("Аргумент должен быть целым числом")  
        if number < 2:
             return "Не простое число"

        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return "Не простое число"
        return "Простое число"
# Пример использования
print(f"{Fore.RED}1 задание{Fore.RESET}")
arr = [2, 3, 4, 2, 2, 11, 12]
sorted_arr = UtilityFunctions.sort_array(arr)
print(sorted_arr)  # Вывод отсортированного массива

# invalid_input = UtilityFunctions.sort_array([])  # Попытка сортировки пустого массива
# print(invalid_input)  # Вывод сообщения "Нельзя ввести пустоту."

# invalid_input = UtilityFunctions.sort_array([2, 3, 4, 2, "5", 11, 12])  # Попытка сортировки массива с нецелыми числами
# print(invalid_input)  # Вывод сообщения "Вводите только целые числа."
#print("\n")

print(f"{Fore.RED}2 задание{Fore.RESET}")
valid_palindrome = UtilityFunctions.is_palindrome("Мадам")
print(valid_palindrome)  # Вывод True (палиндром игнорируя символы и регистр)

# valid_palindrome = UtilityFunctions.is_palindrome("Привет")
# print(valid_palindrome)  # Вывод True (палиндром игнорируя символы и регистр)

# invalid_empty = UtilityFunctions.is_palindrome("  ")
# print(invalid_empty)  # Вывод сообщения "Нельзя вводить пустые значения."

# invalid_symbols = UtilityFunctions.is_palindrome("//??")
# print(invalid_symbols)  # Вывод сообщения "Нельзя вводить символы и знаки препинания."
#print("\n")

print(f"{Fore.RED}3 задание{Fore.RESET}")
factorial = UtilityFunctions.factorial(5)
print(factorial)  # Вывод 120

# factorial = UtilityFunctions.factorial(" ")
# print(factorial)  # Вывод Аргумент должен быть целым числом

# invalid_empty = UtilityFunctions.factorial("asdasd")
# print(invalid_empty)  # Вывод Аргумент должен быть целым числом

# invalid_symbols = UtilityFunctions.factorial(-12)
# print(invalid_symbols)  # Вывод Факториал определен только для неотрицательных чисел
#print("\n")

print(f"{Fore.RED}4 задание{Fore.RESET}")
calculate = UtilityFunctions.calculate(5)
print(calculate)  # Вывод 5

# calculate = UtilityFunctions.calculate(5.2)
# print(calculate)  # Аргумент должен быть целым числом

# calculate = UtilityFunctions.calculate("sdsdsd")
# print(calculate)  # Аргумент должен быть целым числом

# invalid_empty = UtilityFunctions.calculate("")
# print(invalid_empty)  # Вывод Аргумент должен быть целым числом

# invalid_symbols = UtilityFunctions.calculate(-12)
# print(invalid_symbols)  # Позиция должна быть положительным целым числом
#print("\n")

print(f"{Fore.RED}5 задание{Fore.RESET}")
result1 = UtilityFunctions.power(2.2, 2.2)
print(result1)  # Вывод: 5.666

# result2 = UtilityFunctions.power("",2)
# print(result2)  # Вывод: Поля не должны быть пустыми

# result3 = UtilityFunctions.power(2.5, "abc")
# print(result3)  # Вывод: Поля должны содержать числа 
#print("\n")

print(f"{Fore.RED}6 задание{Fore.RESET}")
is_prime_result = UtilityFunctions.is_prime(2)
print(is_prime_result)  # Вывод: Число меньше 2, не может быть простым

# is_prime_result = UtilityFunctions.is_prime(2)
# print(is_prime_result)  # Вывод: Простое число

# is_prime_result = UtilityFunctions.is_prime(21)
# print(is_prime_result)  # Вывод: Не Простое число

# is_prime_result = UtilityFunctions.is_prime(21.2)
# print(is_prime_result)  # Вывод: Аргумент должен быть целым числом

# is_prime_result = UtilityFunctions.is_prime("sdds")
# print(is_prime_result)  # Вывод: Аргумент должен быть целым числом

# is_prime_result = UtilityFunctions.is_prime(" ")
# print(is_prime_result)  # Вывод: Аргумент должен быть целым числом
# print("\n")
  