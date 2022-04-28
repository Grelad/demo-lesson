import unittest
from project.calculator import Calculator


class TestAddOperation(unittest.TestCase):
    def setUp(self):
        self.a = 5

    def test_add(self):
        b = 10
        result = Calculator.add(self.a, b)
        self.assertEqual(result, 15)

    def test_add_with_negative_value(self):
        b = -6
        result = Calculator.add(self.a, b)
        self.assertEqual(result, -1)

    def test_add_with_not_valid_value(self):
        b = "6"
        self.assertRaises(TypeError, Calculator.add, self.a, b)


if __name__ == '__main__':
    unittest.main()
