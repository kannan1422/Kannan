#!/usr/bin/env python
# coding: utf-8

# In[2]:


def is_operator(char):
    return char in "+-*/"

def prefix_to_infix(prefix_expression):
    stack = []

    for char in reversed(prefix_expression):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = f"({operand1}{char}{operand2})"
            stack.append(result)
        else:
            stack.append(char)

    return stack[0]

# Example
prefix_expression = "*+23/45"
infix_expression = prefix_to_infix(prefix_expression)
print(f"Prefix Expression: {prefix_expression}")
print(f"Infix Expression: {infix_expression}")


# In[ ]:




