class DivideCommand:
    name = "divide"

    @staticmethod
    def execute(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

