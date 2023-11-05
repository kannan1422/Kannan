#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

point = Point(6, 9, 12)
result = point.sqSum()
print(result)


# In[ ]:




