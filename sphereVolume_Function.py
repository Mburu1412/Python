"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Python Function to calculate volume of sphere
Formulae : V = (4/3)pi*r*r*r
"""

import math
radius = int(input("Enter radius of sphere : "))

#Function Definition
def volume_of_sphere():
    volume = (4/3) * math.pi * math.pow(radius, 3)
    return volume

#Function Call
volume = volume_of_sphere()
print(f"Volume of Sphere is {volume :.3f}.")
