#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass

def calculate_with_pass(calc_obj):
    calc_obj.add = calc_obj.num1 + calc_obj.num2
    calc_obj.subtract = calc_obj.num2 - calc_obj.num1
    calc_obj.multiply = calc_obj.num1 * calc_obj.num2
    if calc_obj.num1 == 0:
        calc_obj.divide = "Division by zero is not allowed."
    else:
        calc_obj.divide = calc_obj.num2 / calc_obj.num1

obj = Calculator(3, 9)
calculate_with_pass(obj)
print(obj.add)      
print(obj.subtract) 
print(obj.multiply) 
print(obj.divide)  


# In[ ]:




