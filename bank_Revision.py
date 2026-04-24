from datetime import date

class BankAccount:
    def __init__(self, account_number: str, customer_name: str, initial_balance: float = 0.0):
        """
        Initializes a BankAccount object.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.date_of_opening = date.today()

    def deposit(self, amount: float) -> float:
        """
        Adds funds to the balance. Returns the deposited amount.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        return amount

    def withdraw(self, amount: float) -> float | str:
        """
        Deducts funds if sufficient balance exists.
        Returns the withdrawn amount or an insufficient balance message.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        """
        Prints the current account balance.
        """
        print(f"Current balance for account {self.account_number}: ${self.balance:.2f}")

    def customer_details(self):
        """
        Prints customer name, account number, date of opening, and balance.
        """
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Current Balance: ${self.balance:.2f}")

# Example Usage:
my_account = BankAccount("1234567890", "Alice Smith", 1000.00)
my_account.customer_details()
deposited_amount = my_account.deposit(500.00)
print(f"Deposited: ${deposited_amount:.2f}")
my_account.check_balance()
withdrawn_amount = my_account.withdraw(-200.00)
print(f"Withdrawn: ${withdrawn_amount if withdrawn_amount != 'Insufficient balance' else withdrawn_amount}")
my_account.check_balance()
insufficient_withdrawal = my_account.withdraw(2000.00)
print(f"Attempted withdrawal: {insufficient_withdrawal}")
