""" This is the file for my 2nd BankAccount exercise that includes parent/child classes"""

class BankAccount:
    def __init__(self, interest_rate=.02):
        self.balance = 0
        self.interest_rate = interest_rate

    def deposit(self, dep_amount):
        """ incremements self.balance by amount """
        if dep_amount < 0:
            return False
        self.balance += dep_amount
        return self.balance

    def withdraw(self, wit_amount):
        self.balance -= wit_amount
        return self.balance

    def accumulate_interest(self):
        self.balance = self.balance * self.interest_rate
        return self.balance

class ChildrensAccount(BankAccount):
    def __init__(self):
        self.interest_rate = 0
        super().__init__(self.interest_rate)

    def accumulate_interest(self):
        self.balance += 10


class OverdraftAccount(BankAccount):
    def __init__(self, interest_rate=.02, overdraft_penalty=40):
        super().__init__(interest_rate)
        self.overdraft_penalty = overdraft_penalty

    def withdraw(self, wit_amount):
        if self.balance < wit_amount:
            self.balance -= self.overdraft_penalty
            return False
        return super().accumulate_interest()

    def accumulate_interest(self):
        if (self.balance <= 0):
            return False

        return super().accumulate_interest()

Parent = BankAccount(.02)
Childrens = ChildrensAccount()
Overdraft = OverdraftAccount(0)

Overdraft.deposit(200)
Overdraft.withdraw(300)
