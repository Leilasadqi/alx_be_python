class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Performs addition without using class or instance state."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication and prints the class-level calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
