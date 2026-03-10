# Creating Dictionary
student = {
    "name" : "Sir M",
    "Reg_No" : "BSE-01-0024/2025",
    "DOB" : 2007,
    "Program" : "Software Engineering"
    }
print(student)

#Getting specific key
x = student.get("DOB")
print(x)

#Update Dictionary
student.update({"email" : "sirm@example.com"})
print(student)

#Popitem()
student.popitem()
print(student)

#Clear()
student.clear()
print(student)

#Enter Input
student = input("Enter Input:")
print(student)

