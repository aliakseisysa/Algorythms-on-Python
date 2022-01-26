#!/usr/bin/env python
# coding: utf-8

# # Задача 2

# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

# Реализован алгоритм в виде:
# 1) переводим два 16-ричных числа в 10-ричные
# 2) операции сложения и умножения
# 3) переводим результаты обратно в 16-ричные числа

# In[24]:


from collections import defaultdict, deque
import numpy as np


# In[4]:


s = '123456789ABCDEF'


# In[10]:


s[1]


# In[17]:


dd = defaultdict(set)


# In[18]:


pos = 1
for i in s:
    dd[i] = pos
    pos +=1


# In[19]:


print(dd)


# In[236]:


num_1_hex = deque('A2')
num_2_hex = deque('C4F')


# In[237]:


num_1_dec = 0
for i in range(len(num_1_hex)):
    dummy_1 = dd[num_1_hex[-1-i]]*16**i
    num_1_dec += dummy_1

num_2_dec = 0
for i in range(len(num_2_hex)):
    dummy_2 = dd[num_2_hex[-1-i]]*16**i
    num_2_dec += dummy_2


# In[238]:


print(num_1_dec, num_2_dec)


# In[243]:


the_sum = num_1_dec + num_2_dec
print(the_sum)


# In[244]:


the_mult = num_1_dec*num_2_dec
print(the_mult)


# In[245]:


dd_sum = deque()


# In[246]:


last_hex = the_sum % 16
dd_sum.appendleft(last_hex)
the_sum_n = the_sum // 16
while the_sum_n > 0:
    last_hex = the_sum_n % 16
    dd_sum.appendleft(last_hex)
    the_sum_n = the_sum_n // 16


# In[247]:


print(dd_sum)


# In[248]:


dd_mult = deque()


# In[250]:


last_hex_m = the_mult % 16
dd_mult.appendleft(last_hex_m)
the_mult_n = the_mult // 16
while the_mult_n > 0:
    last_hex_m = the_mult_n % 16
    dd_mult.appendleft(last_hex_m)
    the_mult_n = the_mult_n // 16


# In[251]:


print(dd_mult)


# In[299]:


sum_array = []


# In[300]:


for item in dd_sum:
    sum_array.append(list(dd.keys())[list(dd.values()).index(item)])


# In[301]:


print(sum_array)


# In[290]:


for item in dd_sum:
    sum_array.append(list(dd.keys())[list(dd.values()).index(item)])


# In[302]:


mult_array = []


# In[303]:


for item in dd_mult:
    mult_array.append(list(dd.keys())[list(dd.values()).index(item)])


# In[304]:


print(mult_array)


# In[308]:


print(f'Сумма чисел {list(num_1_hex)} + {list(num_2_hex)} = {sum_array}; произведение чисел {list(num_1_hex)} * {list(num_2_hex)} = {mult_array}.')


# In[ ]:




