"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Function to grade the grades of students
"""

grade = int(input ("Enter grade for the student : "))

#Function Definition
def grading_system():
    if grade >= 0 and grade <= 100:
        if grade > 69 :
            print("Grade is A.")
        elif grade > 59:
            print("Grade is B.")
        elif grade > 49:
            print("Grade is C.")
        elif grade > 39:
            print("Grade is D.")
        else:
            print("Grade is E.")
    else:
        print("Enter a Valid Number!")

result = grading_system()
print(result)
