from account import Account

acc1 = Account("Joe", 100, "JoesPassword")
print("Created an account for Joe")
acc2 = Account("Marie", 500, "MariesPassword")
print("Created an account for Marie")


acc1.show()
acc2.show()

# Create a third account by asking the information to the user.

user_name = input("Please enter the user name: ")
balance = int(input("Please enter the initial balance: "))
password = input("Please enter a suitable password for the account: ")

acc3 = Account(user_name, balance, password)

acc3.get_balance("")