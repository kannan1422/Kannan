#!/usr/bin/env python
# coding: utf-8

# In[3]:


def are_rotations(str1, str2):
   
    if len(str1) != len(str2):
        return False

    index = str1.find(str2[0])

    if str1[index:] + str1[:index] == str2:
        return True
    else:
        return False

# Example 
string1 = "abcde"
string2 = "cdeab"

if are_rotations(string1, string2):
    print(f"{string1} and {string2} are rotations of each other.")
else:
    print(f"{string1} and {string2} are not rotations of each other.")


# In[ ]:




