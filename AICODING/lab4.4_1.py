class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        account_holder (str): The name of the account holder.
        balance (float): The current balance of the account.
    """

    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient funds exist."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        """Display the current balance of the account."""
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance:.2f}")


# Sample usage:
if __name__ == "__main__":
    account = BankAccount("Alice", 100.0)
    account.display_balance()
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()