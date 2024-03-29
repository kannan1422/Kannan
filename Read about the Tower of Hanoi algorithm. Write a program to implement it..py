#!/usr/bin/env python
# coding: utf-8

# In[1]:


def tower_of_hanoi(n, source_rod, target_rod, auxiliary_rod):
    if n == 1:
        print(f"Move disk 1 from {source_rod} to {target_rod}")
        return
    tower_of_hanoi(n-1, source_rod, auxiliary_rod, target_rod)
    print(f"Move disk {n} from {source_rod} to {target_rod}")
    tower_of_hanoi(n-1, auxiliary_rod, target_rod, source_rod)

# Example usage:
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')


# In[ ]:




