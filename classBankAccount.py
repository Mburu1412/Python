class BankAccount:
    def __init__(self, account_Number, customer_Name, date_of_opening, balance):
        self.account_Number = account_Number
        self.customer_Name = customer_Name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return amount
        else:
            return "Invalid Deposit Amount!"

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            return amount
        else:
            return "Insufficient Balance"

    def check_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def customer_details(self):
        print(f"Customer Name : {self.customer_Name}.")
        print(f"Account Number : {self.account_Number}.")
        print(f"Date of Opening : {self.date_of_opening}.")
        print(f"Balance : ${self.balance:.2f}.")

#Object Creation
account1 = BankAccount("5rfv", "John Doe", "2026-01-01", 1000)
account1.customer_details()
print(f"Deposited : {account1.deposit(1000)}.")
account1.check_balance()
print(f"Withdraw : {account1.withdraw(500)}.")
account1.check_balance()
print(f"Withdraw : {account1.withdraw(2000)}.")
account1.check_balance()
