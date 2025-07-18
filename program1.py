class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            return self.a / self.b  
        else:
            return "Invalid operation"

a = input("Enter value of a: ")
b = input("Enter value of b: ")
op = input("Enter operation: ")
calc = Calculator(a, b, op)
print("Result is:", calc.calculate())

