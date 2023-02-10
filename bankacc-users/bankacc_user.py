class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account = BankAccount(0.02, 500)
    def withdraw(self, amount):
        self.account.balance -= amount
    def deposit(self, amount):
        self.account.balance += amount
    def display_user_balance(self):
        print('Balance: ', self.account.balance)
    def transfer_money(self,other,amount):
        self.account.balance -= amount
        other.account.balance += amount

class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            return "Insufficient funds"
    def display_account_info(self):
        print('Balance', self.balance)
        print('Interest', self.int_rate)
        return self
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

user1 = User('michael', 'mchoi@mchoi.com')
user2 = User('jonathan', 'jonathan@jonathan.com')
user3 = User('Francis', 'fran@google.com')
account1 = BankAccount()
account2 = BankAccount()


user1.deposit(550)
user1.deposit(150)
user1.deposit(350)
user1.withdraw(35)
user1.display_user_balance()

user2.deposit(10)
user2.deposit(150)
user2.withdraw(50)
user2.withdraw(10)
user2.display_user_balance()

user3.deposit(1110)
user3.withdraw(150)
user3.withdraw(50)
user3.withdraw(10)
user3.display_user_balance()

user1.transfer_money(user3, 500)
user1.display_user_balance()
user3.display_user_balance()

account1.deposit(500).deposit(200).deposit(150).withdraw(500).display_account_info().yield_interest().display_account_info()

account2.deposit(500).deposit(1500).withdraw(100).withdraw(200).withdraw(150).withdraw(50).yield_interest().display_account_info()