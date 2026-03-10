"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Area of Rectangle
"""

length = int(input("Enter length of rectangle : "))
width = int(input("Enter width of rectangle : "))

#Function Definition
def area_of_rectangle():
    area = length * width
    return area

#Function Call
area = area_of_rectangle()
print(f"Area of Rectangle is {area:.2f}")
