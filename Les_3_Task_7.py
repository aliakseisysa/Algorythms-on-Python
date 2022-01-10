#!/usr/bin/env python
# coding: utf-8

# 
# # Задача 7

# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба минимальны), так и различаться.

# In[63]:


import random

array = [random.randint(-10,10) for _ in range(41)]
print(array)


# In[64]:


minimums = []
min_array = array[0]

for i in range(1,41):
    if array[i]<min_array:
        min_array = array[i]

minimums.append(min_array)

pos_min = array.index(min_array)


# In[65]:


array1 = array[0:pos_min]
array2 = array[pos_min+1:41]

print(array1, array2)


# In[66]:


min_array1 = array1[0]

for i in range(1,len(array1)):
    if array1[i]<min_array1:
        min_array1 = array1[i]

minimums.append(min_array1)


# In[67]:


min_array2 = array2[0]

for i in range(1,len(array2)):
    if array2[i]<min_array2:
        min_array2 = array2[i]

minimums.append(min_array2)

print(minimums)


# In[68]:


max_minimums = minimums[0]

for i in range(1,len(minimums)):
    if minimums[i]>max_minimums:
        max_minimums = minimums[i]

minimums.remove(max_minimums)
print(minimums)

