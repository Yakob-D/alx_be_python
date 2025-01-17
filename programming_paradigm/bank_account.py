class BankAccount:
    def __init__(self, account_balance, initial_balance):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
    
    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
