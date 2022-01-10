#!/usr/bin/env python
# coding: utf-8

# # Задача 8

# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

# In[6]:


row1 = []
row2 = []
row3 = []
row4 = []
row5 = []

row1 = [int(item) for item in input("Введите 3 числа первой строки : ").split()]
row2 = [int(item) for item in input("Введите 3 числа второй строки : ").split()]
row3 = [int(item) for item in input("Введите 3 числа третьей строки : ").split()]
row4 = [int(item) for item in input("Введите 3 числа четвертой строки : ").split()]
row5 = [int(item) for item in input("Введите 3 числа пятой строки : ").split()]


# In[9]:


matrix = [row1, row2, row3, row4, row5]


# In[12]:


for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()


# In[15]:


for line in matrix:
    sum_line = 0
    
    for i, item in enumerate(line):
        sum_line += item
        print(f'{item:>5}', end='')
    print(f'    {sum_line}')

