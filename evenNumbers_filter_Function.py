"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Function to filter even numbers 
"""

numbers = []
while True :
    num =int(input("Enter a number (or leave blank to finish) : "))
    if not num:
        break
    numbers.append(num)
    
#Function Definition
def filter_even_numbers(numbers):
    for num in mumbers:
        if num % 2 == 0:
            return numbers
        
#Function Call
print(filter_even_numbers(numbers))
