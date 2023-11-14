#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_operand(char):
    return char.isalnum()

def postfix_to_prefix(postfix_expression):
    stack = []

    for char in postfix_expression:
        if is_operand(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_operand = char + operand1 + operand2
            stack.append(new_operand)

    return stack[0]

# Example usage:
postfix_expression = "23+5*"
prefix_expression = postfix_to_prefix(postfix_expression)
print(f"Postfix Expression: {postfix_expression}")
print(f"Prefix Expression: {prefix_expression}")


# In[ ]:




