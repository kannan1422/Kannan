#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_pairs_with_sum(arr, target_sum):
    arr.sort()
    result_pairs = []
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            result_pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return result_pairs

#Example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10

pairs = find_pairs_with_sum(arr, target_sum)

if pairs:
    print(f"Pairs with sum {target_sum}: {pairs}")
else:
    print(f"No pairs found with sum {target_sum}")


# In[ ]:




