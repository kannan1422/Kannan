#!/usr/bin/env python
# coding: utf-8

# In[1]:


def are_brackets_closed(code):
    stack = []

    #mapping of opening to closing brackets
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    # Iterate
    for char in code:
        # character has closing bracket
        if char in bracket_mapping.keys():
            # Pop the top element from the stack if it is not empty
            top_element = stack.pop() if stack else '#'

            # Compare the popped element 
            if bracket_mapping[char] != top_element:
                return False
        else:
            # it's an opening bracket, push it onto the stack
            stack.append(char)

    #stack is empty, all brackets are closed
    return not stack

# Example
code_snippet = "{[()]}"
result = are_brackets_closed(code_snippet)

if result:
    print("All brackets are closed in the code snippet.")
else:
    print("Not all brackets are closed in the code snippet.")


# In[ ]:




