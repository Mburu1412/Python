"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024

Python Function to calculate area of a circle
"""

import math
radius = int(input("Enter radius of circle : "))

#Function Definition
def area_of_circle():
    area = math.pi * math.pow(radius, 2)
    return area

#Function call
area = area_of_circle()
print(f"Area of Circle is {area:.3f}")
