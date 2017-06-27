""" This is the file for my 2nd BankAccount exercise that includes parent/child classes"""

class BankAccount:
    def __init__(self, interest_rate):
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
        self.balance = self.balance + self.balance * .02
        return self.balance

class ChildrensAccount(BankAccount):
    def __init__(self):
        super().__init__(self)
        self.interest_rate = 0

    def accumulate_interest(self):
        self.balance = self.balance + 10


class OverdraftAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__(interest_rate)
        self.overdraft_penalty = 40

    def withdraw(self, wit_amount):
        if self.balance < wit_amount:
            self.balance -= self.overdraft_penalty
            return False

        self.balance -= wit_amount
        return self.balance

Parent = BankAccount(.02)
Childrens = ChildrensAccount()
Overdraft = OverdraftAccount(0)

Overdraft.deposit(200)
Overdraft.withdraw(300)
