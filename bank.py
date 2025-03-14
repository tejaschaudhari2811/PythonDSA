from account import Account

class Bank:
    def __init__(self):
        self.accounts_dict = {}
        self.next_account_number = 0

    def create_account(self, name, starting_amount, password):
        new_account = Account(name, starting_amount, password)
        self.accounts_dict[self.next_account_number] = new_account
        self.next_account_number +=1
        return self.next_account_number
    
    def open():
        pass

    def close():
        pass

    def deposit():
        pass

    def withdraw():
        pass

    def balance():
        pass

    def show():
        pass