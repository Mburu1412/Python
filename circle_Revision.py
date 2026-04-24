import math

class Circle:
    def __init__(self, radius):
        """
        Initializes a Circle object with a given radius.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def getArea(self):
        """
        Calculates and returns the area of the circle.
        Formula: pi * radius^2
        """
        return math.pi * self.radius**2

    def getCircumference(self):
        """
        Calculates and returns the circumference of the circle.
        Formula: 2 * pi * radius
        """
        return 2 * math.pi * self.radius

# Example Usage:
my_circle = Circle(5)
print(f"Area: {my_circle.getArea()}")
print(f"Circumference: {my_circle.getCircumference()}")
