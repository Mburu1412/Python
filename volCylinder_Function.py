"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Python function to calculate volume of cylinder
Formulae : V = pi*r*r*h
"""

import math
radius = int(input("Enter radius of the cylinder : "))
height = int(input("Enter height of the cylinder : "))

#Function Definition
def volume_of_cylinder():
    volume = math.pi * math.pow(radius, 2) * height
    return volume

#Function Call
volume = volume_of_cylinder()
print(f"Volume of the Cylinder is {volume:.3f}")
