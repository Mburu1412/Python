class BankAcc:
    def __init__(self, balance, name, acc_no):
        self.__balance = balance #Private Attribute
        self._name = name #Protected Attribute
        self.acc_no = acc_no

    def _deposit(self, amount):
        self.__balance += amount
        return f"New Balance : {self.__balance}."

    def get_balance(self):
        return self.__balance

account = BankAcc(1000, "John Doe", 623)
print(account.get_balance())
print(account._deposit(500))
print(account._name)
print(account.acc_no)
