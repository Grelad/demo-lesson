import unittest
from project.calculator import Calculator


class TestMinusOperation(unittest.TestCase):
    def setUp(self):
        self.a = 5

    def test_minus(self):
        b = 10
        result = Calculator.minus(self.a, b)
        self.assertEqual(result, -5)

    def test_minus_with_negative_value(self):
        b = -6
        result = Calculator.minus(self.a, b)
        self.assertEqual(result, 11)

    def test_minus_with_not_valid_value(self):
        b = "6"
        self.assertRaises(TypeError, Calculator.minus, self.a, b)


if __name__ == '__main__':
    unittest.main()
