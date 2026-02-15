"""
Name : Mburu Martin
Adm No : BSCIT-05-0167/2024
Function to find prime numbers in a range of numbers
"""

start = int(input("Enter a Start Number : "))
end = int(input("Enter an End Number : "))

if (start == end):
    print("Start Number should not be equal to the End Number.")
elif (start < end):
    print("Correct Sequence.")
else:
    print("End Number shuold be greater than the Start Number.")

#Function Definition
def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break
                if is_prime:
                    primes.append(num)
    return primes

#Function Call
print(find_primes_in_range(start, end))
