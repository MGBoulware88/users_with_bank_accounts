from bank_account import BankAccount

class User:
    def __init__(self,first,last,email,age,member=False,points=0,account_type="Checking"):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.age = age
        self.is_rewards_member = member
        self.gold_card_points = points
        self.account = [BankAccount(account_type,opening=0,rate=0.02)]

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self,amount):
        if self.gold_card_points >= amount:
            self.gold_card_points-=amount
        else: print("Your balance is too low.")
        return self

    def make_deposit(self, bank_account, amount):
        return self.account[bank_account].deposit(amount)

    def make_withdrawal(self, bank_account, amount):
        return self.account[bank_account].withdraw(amount)

    def display_user_balance(self, bank_account):
        return self.account[bank_account].display_account_info()

    def transfer_money(self, amount, from_account, other_user, to_account):
        if self.account[from_account].balance >= amount:
            self.account[from_account].balance -= amount
            other_user.account[to_account].balance += amount
        else: print("Insufficient funds")

