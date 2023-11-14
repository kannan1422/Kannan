#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def reverse(self):
        if not self.is_empty():
            # Pop the top
            item = self.pop()
            
            #  reverse the of the stack
            self.reverse()

            # Insert the popped element at the bottom
            self.insert_at_bottom(item)

    def insert_at_bottom(self, item):
        if self.is_empty():
        
            self.push(item)
        else:
        
            popped_item = self.pop()
            self.insert_at_bottom(item)

            self.push(popped_item)

# Example
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

print("Original Stack:", my_stack.items)

my_stack.reverse()

print("Reversed Stack:", my_stack.items)


# In[ ]:




