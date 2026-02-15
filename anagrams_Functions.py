"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Function to check if two strings are anagrams of each other
"""

s1 = input("Enter a string 1 : ")
s2 = input("Enter a string 2 : ")

#Define Function
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

#Function Call
print(are_anagrams(s1, s2))
