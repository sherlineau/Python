class User:		
    # constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self


    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Account Balance: ", self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name} transfered {amount} to {other_user.name}")

guido = User("Guido", "guido@example.com")

sherline = User("Sherline", "sherline@example.com")

linda = User("Linda", "linda@example.com")

guido.make_deposit(100).make_deposit(120).make_deposit(400).make_withdrawl(100).display_account_info()

sherline.make_deposit(142).make_deposit(75).make_withdrawl(30).make_withdrawl(200).display_account_info()

linda.make_deposit(1000).make_withdrawl(100).make_withdrawl(400).make_withdrawl(50).display_account_info()

linda.transfer_money(sherline,100)