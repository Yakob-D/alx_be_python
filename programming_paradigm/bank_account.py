import sys

class BankAccount:
    def __init__(self, account_balance, initial_balance=0):  # Set default for initial_balance
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
        print(f"Current Balance: ${self.account_balance:.2f}")

def main():
    account = BankAccount(250)  # Ensure only one argument is required, defaulting initial_balance to 0
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
