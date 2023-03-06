class BankAccount:
    all_accounts = []

    def __init__(self,name,opening,rate=0.01):
        self.name = name
        self.balance = opening
        self.interest_rate = rate
        BankAccount.all_accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else: 
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        return self.balance

    def yield_interest(self):
        interest_rate = self.interest_rate
        if self.balance > 0:
            self.balance += (self.balance * interest_rate)
        return self
    
    @classmethod
    def display_all_accounts_info(cls):
        for account in cls.all_accounts:
            return f"Your {account.name} balance is ${account.balance}."

# checking = BankAccount("Checking",500)
# savings = BankAccount("Savings",10000,0.25)

# checking.deposit(2500).deposit(2500).deposit(2500).withdraw(3000).yield_interest().display_account_info()

# savings.deposit(3000).deposit(3000).withdraw(500).withdraw(500).withdraw(5000).withdraw(6500).yield_interest().display_account_info()

# BankAccount.display_all_accounts_info()