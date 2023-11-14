#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_element = float('inf')

    def push(self, item):
        if item < self.min_element:
            self.min_element = item
        self.stack.append((item, self.min_element))

    def pop(self):
        
        if self.stack:
           
            popped_item, self.min_element = self.stack.pop()
            return popped_item

    def get_min(self):

        return self.min_element

# Example
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
min_stack.push(2)
min_stack.push(1)

print("Current Stack:", [item[0] for item in min_stack.stack])
print("Minimum Element:", min_stack.get_min())

min_stack.pop()
min_stack.pop()

print("After Popping Elements:")
print("Current Stack:", [item[0] for item in min_stack.stack])
print("Minimum Element:", min_stack.get_min())

