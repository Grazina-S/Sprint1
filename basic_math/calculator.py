from decimal import Decimal  # Needed to avoid problems with floating point


class Calculator:
    """A simple calculator for basic arithmetic operations"""

    memory = 0.0

    def add(self, *numbers: float) -> float:
        for number in numbers:
            self.memory += number
        return self.memory

    def substract(self, *numbers: float) -> float:
        if self.memory == 0.0 and len(numbers) > 1:
            self.memory = Decimal(str(numbers[0]))
            for number in numbers[1:]:
                self.memory -= Decimal(str(number))
        else:
            for number in numbers:
                self.memory -= Decimal(str(number))
        return float(self.memory)

    def multiply(self, *numbers: float) -> float:
        if self.memory == 0.0 and len(numbers) > 1:
            self.memory = Decimal(str(numbers[0]))
            for number in numbers[1:]:
                self.memory *= Decimal(str(number))
        else:
            for number in numbers:
                self.memory *= Decimal(str(number))
        return float(self.memory)

    def divide(self, *numbers: float) -> float:
        if any(number == 0.0 for number in numbers):
            raise ZeroDivisionError("You can't divide by 0!")

        if self.memory == 0.0 and len(numbers) > 1:
            self.memory = Decimal(str(numbers[0]))
            for number in numbers[1:]:
                self.memory /= Decimal(str(number))
        else:
            for number in numbers:
                self.memory /= Decimal(str(number))
        return float(self.memory)

    def root(self, number: float = None, root_degree: float = None) -> float:
        """If root degree is not entered,
        function makes square root by default
        """
        if number is None:
            number = self.memory
        if root_degree is None:
            root_degree = 2
        self.memory = number ** (1 / root_degree)
        return self.memory

    def reset(self) -> None:
        """Resets calculator memory back to 0"""
        self.memory = 0.0
