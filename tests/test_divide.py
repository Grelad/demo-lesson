import unittest
from project.calculator import Calculator


class TestDivisionOperation(unittest.TestCase):
    def setUp(self):
        self.a = 5

    def test_division(self):
        b = 10
        result = Calculator.divide(self.a, b)
        self.assertEqual(result, 0.5)

    def test_division_with_negative_value(self):
        b = -5
        result = Calculator.divide(self.a, b)
        self.assertEqual(result, -1)

    def test_division_by_zero(self):
        b = 0
        result = Calculator.divide(self.a, b)
        self.assertEqual(result, "It will cause division by zero exception")


if __name__ == '__main__':
    unittest.main()
