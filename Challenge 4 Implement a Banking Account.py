#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

# for Account
account = Account("Ashish", 5000)
print(f"Account Title: {account.title}")
print(f"Account Balance: {account.balance}")

# for SavingsAccount
savings_account = SavingsAccount("Ashish", 5000, 5)
print(f"Savings Account Title: {savings_account.title}")
print(f"Savings Account Balance: {savings_account.balance}")
print(f"Interest Rate: {savings_account.interestRate}")


# In[ ]:





# In[ ]:




