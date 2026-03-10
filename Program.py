"""
NAME: IAN WABWIRE
ADM NO.: BSCIT-05-0069/2024
"""

# Hello world program

# print ("Hello world")

# print ("My name is Wabz.")
f = open ("C:\\Users\\ianwa\\OneDrive\\Desktop\\Programming Python\\CreateFile.txt", "a")

a = 9
b = 65
name = "Smith"
tall = True
sum = a / b
print (sum)
print ("The sum is ", sum)
print ("Name is" + name + "and sum is " + str(sum), file=f) 
#print ("Name is", name, "and sum is ", sum) 
print (f"The sum is {sum:.2f} And the name is {name}", file=f)


# Python Files (create/open, write, close)
# Modes w-write r-read a-append 
print ("Writing text in a file", file=f)
f.close ()