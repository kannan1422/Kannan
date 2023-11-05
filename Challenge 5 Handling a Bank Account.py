#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return self.balance * (self.interestRate / 100)

#Account
account = Account("Ashish", 2000)
account.deposit(500)
print(f"Balance after deposit: {account.getBalance()}")
account.withdrawal(500)
print(f"Balance after withdrawal: {account.getBalance()}") 

#SavingsAccount
savings_account = SavingsAccount("John", 2000, 5)
interest = savings_account.interestAmount()
print(f"Interest Amount: {interest}") 


# In[ ]:




