# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if funds are available. Return True if successful."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance with 2 decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")