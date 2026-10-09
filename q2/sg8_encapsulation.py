
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = 0
        self.set_balance(balance)

    def set_account_number(self, account_number):
        self.__account_number = account_number

    @property
    def account_number(self):
        return self.__account_number

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Warning: The balance cannot be negative.")

    @property
    def balance(self):
        return self.__balance


# Create an account
account1 = BankAccount(67890, 2500)

print("Bank Account Details")
print("Account Number:", account1.account_number)
print("Balance: {:.2f}".format(account1.balance))

# Update account information
print("\nUpdating account information...")
account1.set_account_number(54321)
account1.set_balance(3500)

print("Account Number:", account1.account_number)
print("Balance: {:.2f}".format(account1.balance))

# Test negative balance
print("\nAttempting to set balance to -500...")
account1.set_balance(-500)

print("Account Number:", account1.account_number)
print("Balance: {:.2f}".format(account1.balance))
