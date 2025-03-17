class AbortTransaction(Exception):
    '''Raise this exception to abort a bank transaction'''
    pass

class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validate_amount(balance)
        self.password = password


    def validate_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction("Amount must be an integer.")
        if amount <= 0:
            raise AbortTransaction("Amount must be positive")
        return amount

    def deposit(self, amount_to_deposit, password):
        if password != self.password:
            print("Incorrect password, please try again")
            return None
        if amount_to_deposit < 0:
            print("The amount cannot be negative,")
            return None
        self.balance += amount_to_deposit
        return self.balance
    
    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            print("Incorrect password. Please try again.")
            return None
    
        if amount_to_withdraw < 0:
            print("You cannot withdraw negative amount.")
            return None
        
        if amount_to_withdraw > self.balance:
            raise AbortTransaction("You cannot withdraw more than your balance")
        
        self.balance -= amount_to_withdraw
        return self.balance
    
    def get_balance(self, password):
        if password != self.password:
            print("Incorrect password. Please try again.")
            return None
        return self.balance
    
    def show(self):
        print(f"This account belongs to {self.name}")


acc1 = Account("Tejas", "2w", "Tejas Chaudhair")
