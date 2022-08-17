#!/usr/bin/env python
# coding: utf-8

# Решение задачи 4 из урока 3: Определить, какое число в массиве встречается чаще всего (и сколько раз).


import random
import timeit
import cProfile


def max_num(n):
    array = [random.randint(-n,n) for _ in range(n)]
    
    counts = []

    for i in array:
        num = array.count(i)
        counts.append(num)
        
    _max_num = counts[0]

    for i in range(1,n):
        if counts[i]>_max_num:
            _max_num = counts[i]
    pos_max = counts.index(_max_num)

    return pos_max, _max_num



#python -m timeit -n 1000 -s "import Les_4_Task_2" "Les_4_Task_2.max_num(100)"  
#1000 loops, best of 3: 134 usec per loop

#python -m timeit -n 1000 -s "import Les_4_Task_2" "Les_4_Task_2.max_num(1000)"  
#1000 loops, best of 3: 8.15 msec per loop

#python -m timeit -n 1000 -s "import Les_4_Task_2" "Les_4_Task_2.max_num(10000)"
#1000 loops, best of 3: 772 msec per loop



#cProfile.run('max_num(1000)')
#     1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
#     1000    0.000    0.000    0.002    0.000 random.py:244(randint)
#     1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    0.032    0.032 {built-in method builtins.exec}
#     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1000    0.028    0.000    0.028    0.000 {method 'count' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1030    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('max_num(10000)')
#    10000    0.009    0.000    0.017    0.000 random.py:200(randrange)
#    10000    0.004    0.000    0.022    0.000 random.py:244(randint)
#    10000    0.006    0.000    0.009    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000    1.083    1.083 {built-in method builtins.exec}
#    10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#    10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#    10000    1.055    0.000    1.055    0.000 {method 'count' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    16488    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

#cProfile.run('max_num(100000)')
#   100000    0.042    0.000    0.081    0.000 random.py:200(randrange)
#   100000    0.021    0.000    0.101    0.000 random.py:244(randint)
#   100000    0.027    0.000    0.039    0.000 random.py:250(_randbelow_with_getrandbits)
#        1    0.000    0.000  105.495  105.495 {built-in method builtins.exec}
#   100000    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
#   100000    0.004    0.000    0.004    0.000 {method 'bit_length' of 'int' objects}
#   100000  105.353    0.001  105.353    0.001 {method 'count' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   131570    0.008    0.000    0.008    0.000 {method 'getrandbits' of '_random.Random' objects}

#Выводы:
#1) с увеличением n в 10 раз время работы функции увеличивается также примерно в 100 раз, т.е. #сложность алгоритма О(n^2);
#2) профилирование показывает, что в коде есть ряд элементов, которые вызываются ровно n раз, а число #вызовов элемента {method 'getrandbits' of '_random.Random' objects} имеет тот же порядок, что и n.


