"""
Модуль с бизнес-логикой калькулятора.
Объект тестирования для Лабораторной работы №6.
"""

import math


class Calculator:
    """Класс с базовыми математическими операциями."""

    def add(self, a, b):
        """Сложение двух чисел."""
        return a + b

    def subtract(self, a, b):
        """Вычитание."""
        return a - b

    def multiply(self, a, b):
        """Умножение."""
        return a * b

    def divide(self, a, b):
        """
        Деление.
        Выбрасывает ZeroDivisionError при делении на ноль.
        """
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def is_prime_number(self, n):
        """
        Проверка, является ли число простым.
        Простое число — это натуральное число > 1, 
        которое делится только на 1 и на само себя.
        """
        if not isinstance(n, int):
            raise TypeError("Число должно быть целым")
        
        if n <= 1:
            return False
            
        if n == 2:
            return True
            
        if n % 2 == 0:
            return False
            
        # Проверяем делители от 3 до корня из n
        for i in range(3, int(math.isqrt(n)) + 1, 2):
            if n % i == 0:
                return False
                
        return True