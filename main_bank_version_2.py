from account import Account

accounts = {}
next_account_number = 0

while True:
    print()
    print("Press b to get balance")
    print("Press d to make deposit")
    print("Press o to open new account")
    print("Press w to make a withdrawl")    
    print("Press s to show all accounts")
    print("Press q to quit")

    action = input("What would you like to do?")
    action = action.lower()[0]
    print()

    if action == "b":
        print("*** Get Balance ***")
        account_number = int(input("Please enter your account number: "))
        user_password = input("Enter password: ")
        account = accounts[account_number]
        if account.password == user_password and account.balance != None:
            account.get_balance()
            