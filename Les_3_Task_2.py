#!/usr/bin/env python
# coding: utf-8

# # Задача 2

# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

# In[10]:


import random

array = [random.randint(1,100) for _ in range(15)]
print(array)


# In[11]:


array_even = []

for i in array:
    if i%2==0:
        pos = array.index(i)
        array_even.append(pos)
print(array_even)


# In[ ]:




