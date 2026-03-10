#Variables
a = 10
b = 20
sum = a + b
name = "John"
tall = True

print(sum)
print("The sum is ",sum)
print("Name is " + name + "and sum is" + str(sum))
print(f"The Sum is {sum:.2f}")
print("Bool is ", tall)

#Python Files: create/open, write, close
f = open("C:\\Users\\Administrator\\OneDrive\\Desktop\\myPython\\sample.txt", "w")
print("This is Sample Text", file=f)
f.close()

#Python Files
r = open("C:\\Users\\Administrator\\OneDrive\\Desktop\\myPython\\example.txt", "w")
print(sum, file=r)
print(f"The Sum is {sum:.3f}", file=r)
print(a, b, sum, file=r)
r.close()
