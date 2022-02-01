#!/usr/bin/env python
# coding: utf-8

# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.

# In[1]:


import sys


# In[2]:


print(sys.version, sys.platform)


# In[3]:


#3.8.9 (default, Oct 26 2021, 07:25:53)
#[Clang 13.0.0 (clang-1300.0.29.30)] darwin


# In[4]:


def show_size(x, level=0):
    
    obj_size = sys.getsizeof(x)
    
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                obj_size = obj_size + sys.getsizeof(key)
                show_size(value, level + 1)
                obj_size = obj_size + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                obj_size = obj_size + sys.getsizeof(item)
                
    return obj_size


# In[6]:


#Урок3 Задача 2
#Во втором массиве сохранить индексы четных элементов первого массива. 
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
#второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), 
#т. к. именно в этих позициях первого массива стоят четные числа.


# In[7]:


import random

array = [random.randint(1,100) for _ in range(15)]


# In[8]:


array_even = []

for i in array:
    if i%2==0:
        pos = array.index(i)
        array_even.append(pos)


# In[30]:


sum_memory = sys.getsizeof(array) + sys.getsizeof(array_even)


# In[10]:


print('Было выделено памяти под объекты: {}'.format(sum_memory))


# In[41]:


#Было выделено памяти под объекты: 368


# In[12]:


#Урок 3 Задача 8
#Матрица 5x4 заполняется вводом с клавиатуры, 
#кроме последних элементов строк. Программа должна вычислять 
#сумму введенных элементов каждой строки и записывать ее 
#в последнюю ячейку строки. В конце следует вывести полученную матрицу.


# In[13]:


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


# In[14]:


#Введите 3 числа первой строки : 11 12 13
#Введите 3 числа второй строки : 23 45 67
#Введите 3 числа третьей строки : 45 89 90
#Введите 3 числа четвертой строки : 50 99 49
#Введите 3 числа пятой строки : 32 45 91


# In[15]:


matrix = [row1, row2, row3, row4, row5]


# In[16]:


for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()


# In[17]:


for line in matrix:
    sum_line = 0
    
    for i, item in enumerate(line):
        sum_line += item
        print(f'{item:>5}', end='')
    print(f'    {sum_line}')


# In[44]:


sum_memory2 = sys.getsizeof(matrix) + sys.getsizeof(row1) + sys.getsizeof(row2) + sys.getsizeof(row3) + sys.getsizeof(row4) + sys.getsizeof(row5)


# In[45]:


print('Было выделено памяти под объекты: {}'.format(sum_memory2))


# In[42]:


#Было выделено памяти под объекты: 536


# In[20]:


#Урок 3 Задача 6


# In[ ]:


#В одномерном массиве найти сумму элементов, 
#находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.


# In[34]:


import random

array = [random.randint(-100,100) for _ in range(41)]


# In[35]:


max_array = array[0]

for i in range(1,41):
    if array[i]>max_array:
        max_array = array[i]
pos_max = array.index(max_array)


# In[36]:


min_array = array[0]

for i in range(1,41):
    if array[i]<min_array:
        min_array = array[i]
pos_min = array.index(min_array)


# In[37]:


new_array = []

if pos_min < pos_max:
    new_array = array[pos_min:pos_max+1]
else:
    new_array = array[pos_max:pos_min+1]


# In[38]:


my_sum = 0
for i in range(1,len(new_array)-1):
    my_sum +=new_array[i]


# In[39]:


sum_memory3 = sys.getsizeof(array) + sys.getsizeof(max_array) + sys.getsizeof(pos_max) + sys.getsizeof(min_array) + sys.getsizeof(pos_min) + sys.getsizeof(new_array) + sys.getsizeof(my_sum)


# In[40]:


print('Было выделено памяти под объекты: {}'.format(sum_memory3))


# In[43]:


#Было выделено памяти под объекты: 700


# Выводы: меньше все памяти было выделено во первом случае, что логично, т.к. работаем со списком из 15 чисел; во втором случае имеем дело с 20 + 4 = 24 числами и со списками, которые содержат ссылки на эти числа. В третьем случае помимо списка из 41 числа создаем несколько переменных, содержащих числа - памяти затрачивается в сравнении больше всего.
