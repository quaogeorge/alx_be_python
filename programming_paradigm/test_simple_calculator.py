import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Required Addition Test ---
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 10), 10)
        self.assertEqual(self.calc.add(-2, -3), -5)

    # --- Subtraction Tests ---
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(5, -2), 7)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    # --- Multiplication Tests ---
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # --- Division Tests ---
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()