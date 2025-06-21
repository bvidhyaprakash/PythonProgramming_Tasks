class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Amount deposited ${amount}, New balance is : ${self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdraw amount ${amount}, Remaining balance is : ${self._balance}")
        else:
            print("Insufficient balance in you account")

    def get_balance(self):
        return self._balance

class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * self.interest_rate/100
        print(f"Calculated Interest : ${interest}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self._balance - amount >= self.min_balance:
            self._balance -= amount
            print(f"Withdraw amount is : ${amount}, Remaining balance is : ${self._balance}")
        else:
            print("Cannot withdraw below min balance")


print("\n Saving Account")
s = SavingAccount("BV1211", 8000, 3000)
s.deposit(4000)
s.withdraw(5000)
s.get_balance()
s.calculate_interest()
s.withdraw(8000)

print("\n Current account")
c = CurrentAccount ("BVn22", 6000, 3000)
c.withdraw(4000)
c.get_balance()
c.withdraw(2500)