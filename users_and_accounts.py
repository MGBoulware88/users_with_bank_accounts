from bank_account import BankAccount
from user import User

gray = User("Gray","Boulware","gray@g.com",34)
toby = User("Toby","Smith","toby@g.com",38)

gray.account.append(BankAccount("Savings",500,0.05))

# print(f"Gray's new balance is ${gray.display_user_balance()}.")
print(gray.display_user_balance(1))

gray.transfer_money(100, 1, toby, 0)
print(gray.display_user_balance(1))
print(toby.display_user_balance(0))