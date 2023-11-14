#!/usr/bin/env python
# coding: utf-8

# In[1]:


def reverse_array_in_place(arr):

    n = len(arr)

    for i in range(n // 2):
        
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

# Example
my_array = [1, 2, 3, 4, 5]
print("Original Array:", my_array)

reverse_array_in_place(my_array)

print("Reversed Array:", my_array)


# In[ ]:




