# oop/class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: does not need class or instance reference"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: has access to class attributes via 'cls'"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

