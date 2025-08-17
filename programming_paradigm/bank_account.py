class BankAccount:
    def __init__(self, initial_balance=0):
        # Start with initial balance (default = 0)
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Take money out if funds are enough"""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Show the current balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")        
