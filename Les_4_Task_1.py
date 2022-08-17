#!/usr/bin/env python
# coding: utf-8

# Решение задачи 6 из урока 3: В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.


import random
import timeit
import cProfile


def sum_range(n):
    array = [random.randint(-n,n) for _ in range(n)]
    max_array = array[0]

    for i in range(1,n):
        if array[i]>max_array:
            max_array = array[i]
    pos_max = array.index(max_array)

    min_array = array[0]

    for i in range(1,n):
        if array[i]<min_array:
            min_array = array[i]
    pos_min = array.index(min_array)
    
    new_array = []

    if pos_min < pos_max:
        new_array = array[pos_min:pos_max+1]
    else:
        new_array = array[pos_max:pos_min+1]
        
    my_sum = 0
    for i in range(1,len(new_array)-1):
        my_sum +=new_array[i]
    return my_sum


#python -m timeit -n 1000 -s "import Les_4_Task_1" "Les_4_Task_1.sum_range(1000)"
#1000 loops, best of 3: 540 usec per loop

#python -m timeit -n 1000 -s "import Les_4_Task_1" "Les_4_Task_1.sum_range(10000)"
#1000 loops, best of 3: 5.54 msec per loop

#python -m timeit -n 1000 -s "import Les_4_Task_1" "Les_4_Task_1.sum_range(100000)"
#1000 loops, best of 3: 54.9 msec per loop


#cProfile.run('sum_range(1000)')
#     1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
#     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
#     1000    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1026    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('sum_range(10000)')
#    10000    0.009    0.000    0.017    0.000 random.py:200(randrange)
#    10000    0.005    0.000    0.022    0.000 random.py:244(randint)
#    10000    0.006    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    16178    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('sum_range(100000)')
#   100000    0.043    0.000    0.083    0.000 random.py:200(randrange)
#   100000    0.022    0.000    0.105    0.000 random.py:244(randint)
#   100000    0.028    0.000    0.040    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.132    0.132 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   100000    0.004    0.000    0.004    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   131174    0.008    0.000    0.008    0.000 {method 'getrandbits' of '_random.Random' objects}


#Выводы:
#1) с увеличением n в 10 раз время работы функции увеличивается также примерно в 10 раз, т.е. #сложность алгоритма О(n);
#2) профилирование показывает, что в коде есть ряд элементов, которые вызываются ровно n раз, а число #вызовов элемента {method 'getrandbits' of '_random.Random' objects} имеет тот же порядок, что и n.
