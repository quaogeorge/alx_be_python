# programming_paradigm/test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_with_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_with_mixed_signs(self):
        self.assertEqual(self.calc.add(-2, 5), 3)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 10), 10)

    # --- Subtraction Tests ---
    def test_subtraction_with_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtraction_with_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_with_mixed_signs(self):
        self.assertEqual(self.calc.subtract(5, -2), 7)

    def test_subtraction_resulting_in_negative(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    # --- Multiplication Tests ---
    def test_multiplication_with_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_with_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, 5), -20)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # --- Division Tests ---
    def test_division_with_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_with_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_with_floats(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()