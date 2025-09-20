class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        # Initialize attributes
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        # Increase balance
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f} into {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Decrease balance if sufficient funds
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f} from {self.account_holder}'s account.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        # Print account details
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance:.2f}")
        print("-" * 40)


if __name__ == "__main__":
    # Create two bank account objects
    account1 = BankAccount("Alice", 1000.0, "Savings")
    account2 = BankAccount("Bob", 500.0, "Current")

    # Display initial balances
    print("Initial Account Details:")
    account1.display_balance()
    account2.display_balance()

    # Perform operations on account1
    print("Performing operations on Alice's account...")
    account1.deposit(200)
    account1.withdraw(150)
    account1.display_balance()

    # Perform operations on account2
    print("Performing operations on Bob's account...")
    account2.deposit(300)
    account2.withdraw(1000)  # This will fail due to insufficient balance
    account2.display_balance()
