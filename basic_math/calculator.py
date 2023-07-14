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
    
    def root(self, number: float) -> float:
        self.memory **= (1 / number)
        return self.memory
    
    def reset(self):
        self.memory = 0.0
    
    
        
    
    
    
    
# calculator = Calculator()
# result = calculator.add(7,3)
# print(result)