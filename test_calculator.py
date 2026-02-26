import pytest
from quick_calc import Calculator


@pytest.fixture
def calc():
    return Calculator()


# --- Basic operations (at least 1 per operation) ---


def test_add_integers(calc):
    assert calc.add(2, 3) == 5


def test_subtract_integers(calc):
    assert calc.subtract(10, 4) == 6


def test_multiply_integers(calc):
    assert calc.multiply(6, 7) == 42


def test_divide_integers(calc):
    assert calc.divide(8, 2) == 4


# --- Edge cases (at least 2) ---


def test_divide_by_zero_raises(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


def test_negative_numbers(calc):
    assert calc.add(-5, -3) == -8
    assert calc.subtract(-5, 3) == -8


def test_decimal_numbers(calc):
    assert calc.multiply(0.5, 0.2) == pytest.approx(0.1)
    assert calc.divide(1.0, 4.0) == pytest.approx(0.25)


def test_very_large_numbers(calc):
    big = 10**18
    assert calc.add(big, big) == 2 * big
