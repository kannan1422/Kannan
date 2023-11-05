#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Student:
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setRollNumber(self, roll_number):
        self._rollNumber = roll_number

    def getRollNumber(self):
        return self._rollNumber

    name = property(getName, setName)
    rollNumber = property(getRollNumber, setRollNumber)

# Example usage:
student = Student()
student.name = "Vijay"
student.rollNumber = 63450

name = student.name
roll_number = student.rollNumber

print(name)       
print(roll_number)


# In[ ]:




