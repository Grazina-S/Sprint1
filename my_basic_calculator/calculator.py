class Calculator:
    """A simple calculator for basic arithmetic operations"""

    def __init__(self):
        self.memory = 0.0

    def add(self, *numbers: float) -> float:
        # Adds the numbers
        for number in numbers:
            self.memory += number
        return self.memory

    def subtract(self, *numbers: float) -> float:
        # Subtraction: all entered numbers serve as subtrahends
        # number in memory serve as minuend
        for number in numbers:
            self.memory -= number
        return self.memory

    def multiply(self, *numbers: float) -> float:
        # Multiplies all numbers
        for number in numbers:
            self.memory *= number
        return self.memory

    def divide(self, *numbers: float) -> float:
        # Division: entered numbers serve as divisors
        # number in memory serve as dividend
        for number in numbers:
            if number == 0:
                raise ValueError("Can't divide by zero!")
            self.memory /= number
        return self.memory

    def root(self, number: int) -> float:
        # Root of nth degree
        # entered number serve as degree
        if number == 0:
            raise ValueError("The degree of the root can't be 0")
        self.memory = self.memory ** (1 / number)
        return self.memory

    def reset(self) -> float:
        """Resets calculator memory back to 0"""
        self.memory = 0.0
