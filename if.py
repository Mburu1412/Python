#Mburu Martin
#BSCIT-05-0167/2024

# Input marks for three subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Calculate average
average = (sub1 + sub2 + sub3) / 3

# Determine grade
if 70 <= average <= 100:
    grade = "A"
elif 60 <= average <= 69:
    grade = "B"
elif 50 <= average <= 59:
    grade = "C"
elif 40 <= average <= 49:
    grade = "D"
elif 0 <= average <= 39:
    grade = "Fail"
else:
    grade = "Invalid score"

# Output results
print("Average Score:", average)
print("Grade:", grade)
