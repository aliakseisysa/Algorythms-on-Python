#!/usr/bin/env python
# coding: utf-8

# # Задача 9

# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# In[18]:


import random

matrix = [[random.randint(1,10) for _ in range(5)] for _ in range(7)]


# In[19]:


for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()


# In[20]:


for i, line in enumerate(matrix):

    if i == 0:                              
        min_line = line.copy()
        for item in line:
            print(f'{item:>5}', end='')
        print()
        continue

    for idx, item in enumerate(line):
        if item < min_line[idx]:            
            min_line[idx] = item            
        print(f'{item:>5}', end='')
    print()

print('-' * len(min_line) * 5)

max_min = min_line[0]
for item in min_line:
    print(f'{item:>5}', end='')
    if item > max_min:
        max_min = item

print()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_min}')

