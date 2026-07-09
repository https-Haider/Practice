class BankAccount:
    def __init__(self,balance):
        self._balance = balance  # Private attribute
    def deposit(self,amount):
        self._balance+=amount
    def withdraw(self,amount):
        if amount<=self._balance:
            self._balance-=amount
    def get_balance(self):
        return self._balance

account=BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())
