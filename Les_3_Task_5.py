#!/usr/bin/env python
# coding: utf-8

# # Задача 5

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# In[14]:


import random

array = [random.randint(-100,100) for _ in range(41)]
print(array)


# In[15]:


array_below = []

for i in array:
    if i<0:
        array_below.append(i)
print(array_below)

len_array_below = len(array_below)


# In[18]:


max_num = array_below[0]

for i in range(1,len_array_below):
    if array_below[i]>max_num:
        max_num = array_below[i]
    pos_max = array.index(max_num)
print(f"Максимальный отрицательный элемент {max_num} находится на позиции {pos_max}.")

