class Bank_Account():
#  all_instances is partf of the ninja bonus             
    all_instances =  []      


    def __init__(self,int_rate, balance = 0): # the vaule of the balance will default to zero if no amount is given which is why i put = 0 
      self.int_rate = int_rate
      self.balance = balance
      Bank_Account.all_instances.append(self)
      #  all instances is part of the ninaj bonus            
    def deposit(self, amount):
      self.balance += amount
      return self
    
    def withdraw(self, amount):
      if (self.balance - amount) > 0:
        self.balance -= amount
      else: 
        print(f'Sorry, insuffecient funds to withdraw money. Your Broke! Your balance: {self.balance}')
      return self
    #  if less than zero i cant wiyhdraw no money so i write if else statement to print insuffecient funds
    def display_account_info(self):
      print(self.balance)
      return self
    #   just displays my balance
    def yield_interest(self):
      if self.balance > 0:
        self.balance += (self.balance * self.int_rate)
      else: 
        print('Your account balance is negative')
      return self
      #  if greater than zero i will yield insterest if i have no money the else function activates and it prints my accopunt is in negatives

#  ninaj bonus followed my teachers vid he explains class methods well
    @classmethod
    def print_instances(cls):
      for i in cls.all_instances:
        print(i.display_account_info())


Miguel = Bank_Account(.2, 100)
John = Bank_Account(0.5, 200)

Bank_Account.print_instances()
#  ninja bonus ^^^^^^^^^^

Miguel.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
John.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(20).withdraw(20).yield_interest().display_account_info()
