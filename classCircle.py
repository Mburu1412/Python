"""
Python Class to Calculate Area and Circumference of A Circle
"""

#Class Creation
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        area = math.pi * math.pow(self.radius, 2)
        return f"The Area is {area:.2f}"

    def Circumference(self):
        circumference = 2 * math.pi * self.radius
        return f"The Circumference is {circumference:.2f}"

#Object Creation
myCircle = Circle(7)
print(myCircle.Area())
print(myCircle.Circumference())
