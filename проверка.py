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

        for i in range(2, int(number**0.11) + 1):
            if number % i == 0:
                return "Не простое число"
        return "Простое число"