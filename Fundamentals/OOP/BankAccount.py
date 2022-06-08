class User:		
    # constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0,balance=0)

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)
        return self


    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_account_info(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
        self.account.display_account_info()
        return self

class BankAccount:

    list_accounts = []

    def __init__(self, int_rate, balance = 0):
        self.balance = balance
        self.interest = int_rate
        BankAccount.list_accounts.append( self )

    def display_account_info(self):
        print(f"Balance: {self.balance:.2f}") # :.2f limits to 2 decimals
        return self

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * (self.interest/100))
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.list_accounts: 
            # student represents an object
            print(f"{account.name} Balance: {account.balance:.2f}")

# sherline = BankAccount( "Sherline", 2.5,1000).deposit(100).deposit(200).deposit(899).withdraw(120).yield_interest()
# linda = BankAccount( "Linda" , 3 ).deposit(1000).deposit(250).withdraw(100).withdraw(10).withdraw(102).withdraw(25).yield_interest()

# BankAccount.print_all_accounts()

sherline = User("Sherline","sherline@email.com")
sherline.make_deposit(1000).display_account_info()