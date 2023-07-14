class Calculator:
    """A simple calculator for basic arithmetic operations"""
    memory = 0.0
    
    def add(self, *numbers: float) -> float:
        for number in numbers:
            self.memory += number
        return self.memory
    
    def subtract(self, *numbers: float) -> float:
        for number in numbers:
            self.memory -= number
        return self.memory
    
    def multiply(self, *numbers: float) -> float:
        for number in numbers:
            self.memory *= number
        return self.memory
    
    def divide(self, *numbers: float) -> float:
        for number in numbers:
            self.memory /= number
        return self.memory
    
    def root(self, number: float = None, root_degree: float = None) -> float:
        """If root degree is not entered, function makes square root by default"""
        if number is None:
            number = self.memory
        if root_degree is None:
            root_degree = 2         
        self.memory = number ** (1 / root_degree)        
        return self.memory
    
    def reset(self) -> None:
        """Resets calculator memory back to 0"""
        self.memory = 0.0