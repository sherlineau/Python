class User:		
    # constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        # print("Amount deposited: ", amount)


    def make_withdrawl(self, amount):
        self.account_balance -= amount
        # print("Amount withdrawn: ", amount)

    def display_account_info(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Account Balance: ", self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{amount} was transferred")
        print(f"{other_user.name}'s new balance is {other_user.account_balance}")
        


adrian = User("Adrian", "Adrian@example.com")

sherline = User("Sherline", "sherline@example.com")

linda = User("Linda", "linda@example.com")

adrian.make_deposit(100)
adrian.make_deposit(120)
adrian.make_deposit(400)
adrian.make_withdrawl(100)
adrian.display_account_info()

sherline.make_deposit(142)
sherline.make_deposit(75)
sherline.make_withdrawl(30)
sherline.make_withdrawl(200)
sherline.display_account_info()

linda.make_deposit(1000)
linda.make_withdrawl(100)
linda.make_withdrawl(400)
linda.make_withdrawl(50)
linda.display_account_info()

linda.transfer_money(sherline,100)