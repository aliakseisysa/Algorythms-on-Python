#!/usr/bin/env python
# coding: utf-8

# # Задача 1

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

# In[327]:


from collections import defaultdict
import numpy as np


# In[328]:


data = []


# In[329]:


num = int(input('Enter the quantity of factories:'))


# In[330]:


for i in range(num):
    names = [input('Enter the name of factory: ')]
    data.extend(names)


# In[339]:


income = dict.fromkeys(data)
inc = defaultdict(list) #defaultdict использован для добавления для каждого предприятия 
                        #массива из 4-х чисел (поквартальная прибыль)
for k in income:
    for i in range(1,5):
        dummy = int(input(f'Enter the {i} quartile income for {k} factory: ')) #предполагается, что пользователь поочередно вводит 
                                                                            #поквартальные данные о прибыли каждого предприятия 
        inc[k].append(dummy)
        


# In[340]:


print(inc)


# In[341]:


keys_inc = list(inc.keys())
values_inc = list(inc.values())


# In[342]:


mean_inc = np.sum(values_inc)/len(values_inc)
print(mean_inc)


# In[343]:


income_year =  {}

for k in keys_inc:
    j = keys_inc.index(k)
    summa = 0
    for i in range(4):
        summa += values_inc[j][i]
    income_year[k] = summa
        


# In[344]:


print(income_year)


# In[345]:


keys_inc_year = list(income_year.keys())
values_inc_year = list(income_year.values())


# In[346]:


mean_lower =  []
mean_upper = []

for k in keys_inc_year:
    j = keys_inc_year.index(k)
    if values_inc_year[j] < mean_inc:
        mean_lower.append(k)
    elif values_inc_year[j] > mean_inc:
        mean_upper.append(k)
    else:
        print(f'Предприятие {k} имеет среднюю прибыль')
print(f'Прибыль предприятий {mean_lower} ниже среднего, а предприятий {mean_upper} выше среднего.')


# In[ ]:




