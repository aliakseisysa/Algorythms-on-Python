#!/usr/bin/env python
# coding: utf-8

# # Задача 4

# Определить, какое число в массиве встречается чаще всего.

# In[53]:


import random

array = [random.randint(1,20) for _ in range(50)]
print(array)


# In[54]:


counts = []

for i in array:
    num = array.count(i)
    counts.append(num)


# In[55]:


max_num = counts[0]

for i in range(1,50):
    if counts[i]>max_num:
        max_num = counts[i]
pos_max = counts.index(max_num)


# In[56]:


print(f'Число {array[pos_max]} встречается чаще всего: {max_num} раз(а).')

