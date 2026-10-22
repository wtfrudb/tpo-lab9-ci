"""
Модульные тесты для класса Calculator.
Проверяют базовые арифметические операции и логику проверки на простоту.
"""

from calculator import Calculator


# ============================================
# Тесты для метода add (сложение)
# ============================================
def test_add_positive_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_add_negative_numbers():
    calc = Calculator()
    assert calc.add(-2, -3) == -5

def test_add_zero():
    calc = Calculator()
    assert calc.add(5, 0) == 5


# ============================================
# Тесты для метода subtract (вычитание)
# ============================================
def test_subtract_positive_numbers():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_subtract_resulting_in_negative():
    calc = Calculator()
    assert calc.subtract(3, 10) == -7


# ============================================
# Тесты для метода multiply (умножение)
# ============================================
def test_multiply_positive_numbers():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_multiply_by_zero():
    calc = Calculator()
    assert calc.multiply(100, 0) == 0

def test_multiply_negative():
    calc = Calculator()
    assert calc.multiply(-5, 3) == -15


# ============================================
# Тесты для метода divide (деление)
# ============================================
def test_divide_positive_numbers():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0

def test_divide_resulting_in_fraction():
    calc = Calculator()
    # Используем pytest.approx для сравнения чисел с плавающей точкой
    import pytest
    assert calc.divide(10, 3) == pytest.approx(3.333333, rel=1e-5)


# ============================================
# Тесты для метода is_prime_number (проверка на простоту)
# ============================================
def test_is_prime_number_true_for_primes():
    calc = Calculator()
    assert calc.is_prime_number(2) is True
    assert calc.is_prime_number(3) is True
    assert calc.is_prime_number(13) is True
    assert calc.is_prime_number(97) is True

def test_is_prime_number_false_for_composites():
    calc = Calculator()
    assert calc.is_prime_number(4) is False
    assert calc.is_prime_number(10) is False
    assert calc.is_prime_number(100) is False

def test_is_prime_number_edge_cases():
    calc = Calculator()
    # Отрицательные числа, 0 и 1 не являются простыми
    assert calc.is_prime_number(-5) is False
    assert calc.is_prime_number(0) is False
    assert calc.is_prime_number(1) is False