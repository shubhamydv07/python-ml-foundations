class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount!"
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount!"
        if self.__balance >= amount:
            self.__balance -= amount
            return f"Withdrawn {amount}. New balance: {self.__balance}"
        else:
            return "Insufficient balance!"

    def get_balance(self):
        return f"Current balance: {self.__balance}"

    def get_account_number(self):
        return f"Account number: {self.__account_number}"


account = BankAccount(125114029, 1303000)
print(account.deposit(10000))
print(account.withdraw(5000))
print(account.get_balance())
print(account.get_account_number())