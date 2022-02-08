class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self , name, email_address = None):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0
        
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"{self.name} Balance: {self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance = self.account_balance - amount
        other_user.account_balance = other_user.account_balance + amount

adrien = User("Adrien")
mrNibbles = User("Mr. Nibbles", "nibbles@python.com")
benny = User("Benny Bob", "benny@python.com")

adrien.make_deposit(305)
adrien.display_user_balance()

mrNibbles.make_deposit(1200)
mrNibbles.display_user_balance()

benny.make_withdrawal(7500)
benny.display_user_balance()

mrNibbles.make_withdrawal(400)
mrNibbles.display_user_balance()

adrien.make_deposit(400)
adrien.display_user_balance()

adrien.transfer_money(mrNibbles,100)
adrien.display_user_balance()
mrNibbles.display_user_balance()