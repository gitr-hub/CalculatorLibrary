"""
Unit tests for the calculator library
"""

import calculator

class TestCalculator:

    def test_addition(self):
        assert 5 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 3 == calculator.subtract(4, 2)
