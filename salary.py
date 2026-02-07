#Mburu Martin
#BSCIT-05-0167/2024
salary = float(input("Please enter your salary: "))
yearOfService = int(input("Enter year(s) of service: "))

if yearOfService > 10:
    bonus = salary * 0.10
elif 6 <= yearOfService <= 10:
    bonus = salary * 0.08
else:
    bonus = salary * 0.05

print(f"Your bonus amount is: Ksh. {bonus:.2f}")

# Writing into file
f = open("printInFile.txt", "a")

print(f"Your salary is: {salary:.2f} and years of service: {yearOfService}", file=f)
print(f"Your bonus amount is: Ksh. {bonus:.2f}", file=f)

f.close()
