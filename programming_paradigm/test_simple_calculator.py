# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(0, 7), -7)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 6), -12)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Edge case: division by zero should return None
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == "__main__":
    unittest.main()

