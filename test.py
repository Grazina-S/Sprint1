import unittest

from my_basic_calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test all functions from calculator module"""

    def setUp(self):
        self.calculator = Calculator()

    def test_all(self):
        result = self.calculator.add(2, 6)  # Test addition
        self.assertAlmostEqual(result, 8.0, places=6)
        result = self.calculator.root(3)  # Test root
        self.assertAlmostEqual(result, 2.0, places=6)
        result = self.calculator.subtract(-7)  # Test subtract
        self.assertAlmostEqual(result, 9.0, places=6)
        result = self.calculator.multiply(2, 3)  # Test multiply
        self.assertAlmostEqual(result, 54.0, places=6)
        result = self.calculator.divide(6)  # Test divide
        self.assertAlmostEqual(result, 9.0, places=6)
        self.calculator.reset()
        result = self.calculator.multiply(2.15651)
        self.assertAlmostEqual(result, 0.0, places=6)  # Test if reset to 0.0


if __name__ == "__main__":
    unittest.main()
