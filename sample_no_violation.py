"""
This is a sample Python file that follows PEP-8 guidelines.
Each function and class starts with a docstring.
"""

def hello_world():
    """Print a greeting."""
    print("Hello, world!")

class Greeter: # pylint: disable=too-few-public-methods
    """A class for greeting people."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.name}!")

if __name__ == "__main__":
    greeter = Greeter("Alice")
    greeter.greet()
