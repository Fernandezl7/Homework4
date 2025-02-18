'''Test Calculation'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# pylint: disable=unnecessary-dunder-call, invalid-name
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),  # Test addition
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),  # Test subtraction
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  # Test multiplication
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),  # Test division
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),  # Test addition with decimals
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),  # Test subtraction with decimals
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Test multiplication with decimals
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Test division with decimals
])
def test_calculation_operations(a, b, operation, expected):
    '''Test calculation operation'''
    calc = Calculation(a, b, operation)  # Create a Calculation instance .
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    ''' Test the string representation (__repr__) of the Calculation class.'''    
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ output does not match expected string."

def test_divide_by_zero():
    '''Test division by zero to ensure it raises a ValueError.'''
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.
