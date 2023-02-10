class BankAccount:
    def __init__(self,name, int_rate=0, balance=0):
        self.name = name
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        self.balance -= amount
        if amount > self.balance:
            self.balance -= 5
            print("Insufficient Funds Charging a $5 fee")  
        return self   
    def display_user_balance(self):
        self.balance
        print(f"Balance: ${self.balance} for {self.name}")
        return self
    def yield_interest(self):
        if self.balance > 0:    
            self.balance = self.balance + (self.balance * self.int_rate)
        return self
Account1=BankAccount('miguel',.02, balance=0)
Account2=BankAccount('john', .05, 0)
# Account1.deposit(100)
# Account1.withdrawl(105)
# print(Account1.balance)
Account1.deposit(500).deposit(50).deposit(50).withdrawl(100).yield_interest().display_user_balance()
Account2.deposit(500).deposit(500).withdrawl(100).withdrawl(100).withdrawl(100).withdrawl(100).yield_interest().display_user_balance()
print(Account1, Account2)
