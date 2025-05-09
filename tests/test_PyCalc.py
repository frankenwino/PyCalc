import pytest
from app.PyCalc import PyCalculator

@pytest.fixture
def calc():
    return PyCalculator()

def test_initial_result(calc):
    assert calc.result == 0

def test_add(calc):
    assert calc.add(5) == 5
    assert calc.add(3) == 8

def test_subtract(calc):
    calc.add(10)  # Set initial value
    assert calc.subtract(4) == 6
    assert calc.subtract(2) == 4

def test_multiply(calc):
    calc.add(2)  # Set initial value
    assert calc.multiply(3) == 6
    assert calc.multiply(2) == 12

def test_divide(calc):
    calc.add(10)  # Set initial value
    assert calc.divide(2) == 5
    assert calc.divide(5) == 1

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(0)

def test_clear(calc):
    calc.add(10)
    calc.clear()
    assert calc.result == 0
