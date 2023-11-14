#!/usr/bin/env python
# coding: utf-8

# In[3]:


def first_non_repeated_char(s):
    for char in s:
        if s.count(char) == 1:
            return char

    return None

# Example
input_string = "Programming"

result = first_non_repeated_char(input_string)

if result:
    print(f"The first non-repeated character in '{input_string}' is: {result}")
else:
    print(f"There is no non-repeated character in '{input_string}'.")


# In[ ]:




