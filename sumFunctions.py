"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Function to add list of numbers
"""

def sum_of_list(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (Numbers)
print(sum_of_list(1, 2, 3, 4, 5, 6, 7, 8))
    
