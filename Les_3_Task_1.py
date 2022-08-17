#!/usr/bin/env python
# coding: utf-8

# # Задача 1

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

# In[4]:


nat = [i for i in range(2,100)]
print(nat)


# In[21]:


spam = []
for i in range(2,10):
    for j in nat:
        if j%i==0:
            spam.append(j)
    print(len(spam))
    spam = []

