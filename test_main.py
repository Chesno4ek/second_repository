import pytest
from main import calculate_area  # Импорт функции из твоего кода

def test_calculate_area():
    assert calculate_area(5, 4) == 20
    assert calculate_area(2, 10) == 20
    assert calculate_area(0, 5) == 0
    assert calculate_area(-1, 5) == 0  # Ожидаем 0, если отрицательные значения

if __name__ == "__main__":
    pytest.main()
