#Mburu Martin
#BSCIT-05-0167/2024

# Assign a winning number
winning_number = 7

# Ask user to guess
guess = int(input("Guess a number: "))

# Check guess
if guess == winning_number:
    print("YOU WIN!!!!")
else:
    if guess < winning_number:
        print("too low")
    else:
        print("too high")
