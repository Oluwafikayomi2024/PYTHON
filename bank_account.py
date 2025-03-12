class Account:
    def __init__(self, account_number: str, account_balance: float, account_holder: str):
        # Initializing the attributes
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, amount: float):
        """Method to deposit an amount into the account."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.account_balance}")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount: float):
        """Method to withdraw an amount from the account."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.account_balance}")
        else:
            print(f"Insufficient funds. Current balance: ${self.account_balance}")

    def check_balance(self):
        """Method to check the current account balance."""
        return self.account_balance


# Create an instance of the Account class
my_account = Account("12345", 1000.0, "John Doe")

# Test the methods
print(f"Initial balance: ${my_account.check_balance()}")  # Check initial balance

# Deposit money
my_account.deposit(500.0)

# Withdraw money
my_account.withdraw(200.0)

# Check balance again after transactions
print(f"Final balance: ${my_account.check_balance()}")
