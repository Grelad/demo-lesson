from abc import ABC


class Calculator(ABC):

    @staticmethod
    def add(a: int, b: int):
        """Add operation"""
        return a + b

    @staticmethod
    def minus(a: int, b: int):
        """Minus operation"""
        return a - b

    @staticmethod
    def multiply(a: int, b: int):
        """Multiply operation"""
        return a * b

    @staticmethod
    def divide(a: int, b: int):
        """Division operation"""
        if b == 0:
            return "It will cause division by zero exception"
        return a / b
