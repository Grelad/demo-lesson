import unittest
from project.calculator import Calculator


class TestMultiplyOperation(unittest.TestCase):
    def setUp(self):
        self.a = 5

    def test_multiply(self):
        b = 10
        result = Calculator.multiply(self.a, b)
        self.assertEqual(result, 50)

    def test_multiply_with_negative_value(self):
        b = -6
        result = Calculator.multiply(self.a, b)
        self.assertEqual(result, -30)

    def test_unpredictable_multiply_with_not_valid_value(self):
        b = "6"
        result = Calculator.multiply(self.a, b)
        self.assertNotEqual(type(result), type(30))


if __name__ == '__main__':
    unittest.main()
