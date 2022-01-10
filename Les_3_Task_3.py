#!/usr/bin/env python
# coding: utf-8

# # Задача 3

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# In[15]:


import random

array = [random.randint(1,100) for _ in range(15)]
print(array)


# In[16]:


max_array = array[0]

for i in range(1,15):
    if array[i]>max_array:
        max_array = array[i]
pos_max = array.index(max_array)


# In[17]:


min_array = array[0]

for i in range(1,15):
    if array[i]<min_array:
        min_array = array[i]
pos_min = array.index(min_array)


# In[18]:


array[pos_min] = max_array
array[pos_max] = min_array
array

