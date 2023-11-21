#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

def regex_query_tool():
    try:
        # Get user input for the text and regex pattern
        text = input("Enter the text string: ")
        pattern = input("Enter the regex pattern: ")

        # Run the regex pattern against the text
        matches = re.findall(pattern, text)

        # Print the matches
        if matches:
            print("Matches found:")
            for match in matches:
                print(match)
        else:
            print("No matches found.")

    except re.error as e:
        # Handle regex errors
        print(f"Regex error: {e}")

if __name__ == "__main__":
    regex_query_tool()


# In[ ]:




