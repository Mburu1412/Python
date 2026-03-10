#Simple Interest Function
principal = int(input("Enter Principal Amount : "))
rate = int(input("Enter Rate : "))
time = int(input("Enter Time in Years : "))

#Create Function simple_Interest()
def simple_Interest(principal, rate, time):
    interest = principal * rate/100 *time
    return interest

#Function Call
interest = simple_Interest(principal, rate, time)
print(interest)
