#!/usr/bin/env python
# coding: utf-8

# # Задача 6

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

# In[35]:


import random

array = [random.randint(-100,100) for _ in range(41)]
print(array)


# In[36]:


max_array = array[0]

for i in range(1,41):
    if array[i]>max_array:
        max_array = array[i]
pos_max = array.index(max_array)


# In[37]:


min_array = array[0]

for i in range(1,41):
    if array[i]<min_array:
        min_array = array[i]
pos_min = array.index(min_array)


# In[38]:


new_array = []

if pos_min < pos_max:
    new_array = array[pos_min:pos_max+1]
else:
    new_array = array[pos_max:pos_min+1]
print(new_array)


# In[41]:


my_sum = 0
for i in range(1,len(new_array)-1):
    my_sum +=new_array[i]
print(f"Сумма {len(new_array)} элементов массива, находящихся между минимальным и максимальным элементами, составляет {my_sum}.")

