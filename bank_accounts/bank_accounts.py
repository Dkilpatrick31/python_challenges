""" This is my bank accounts program """

class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0

    def deposit(self, dep_amount):
        """incremements self.balance """
        if self.overdraft_fees > 0:
            dep_amount -= self.overdraft_fees
            if dep_amount < 0:
                self.overdraft_fees = dep_amount * -1
                dep_amount = 0
        self.balance += dep_amount


    def withdraw(self, wit_amount):
        self.balance -= wit_amount
        if self.balance < 0:
            self.overdraft_fees += 20
        return wit_amount

    def check_balance(self):
        total_balance = self.balance - slef.overdraft_fees

    def transfer(other_bank_account, amount):
        self.balance += other_bank_account.withdraw(amount)


checking = BankAccount('checking')
saving = BankAccount('saving')
Hello_this_is_dane_account = BankAccount('Danes Account')

checking.deposit(200)
checking.withdraw(100)

savings.deposit(150)
savings.withdraw(100)

checking.deposit(savings)

checking.transfer(checking, 10)

checking.check_balance()
savings.check_balance()
