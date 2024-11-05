import pytest
from calculator import add, subtract, multiply, divide, power, factorial  # Импортируем функции

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(0, 1) == -1
    assert subtract(1, 1) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(-1, 1) == -1

# Проверяем, что ValueError выбрасывается при делении на ноль
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(-3, 3) == -27

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1

    with pytest.raises(ValueError):
        factorial(-1)  # Факториал отрицательного числа должен вызывать ошибку
