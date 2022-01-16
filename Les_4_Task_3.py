#!/usr/bin/env python
# coding: utf-8

# Решение задачи 4 из урока 2. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 


import timeit
import cProfile



def summ(n):
    _sum = 0
    for i in range(n+1):
        if i == 0:
            a = 1
        elif i%2==1:
            a = -a/2
        else:
            a = -a/2
        _sum += a
    return(_sum)


#python -m timeit -n 1000 -s "import Les_4_Task_3" "Les_4_Task_3.summ(1000)"   
#1000 loops, best of 3: 67.6 usec per loop

#python -m timeit -n 1000 -s "import Les_4_Task_3" "Les_4_Task_3.summ(10000)"
#1000 loops, best of 3: 657 usec per loop

#python -m timeit -n 1000 -s "import Les_4_Task_3" "Les_4_Task_3.summ(100000)"
#1000 loops, best of 3: 6.58 msec per loop


#cProfile.run('summ(1000)')
#         4 function calls in 0.000 seconds
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 1136749821.py:1(summ)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('summ(100000)')
#         4 function calls in 0.025 seconds
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.025    0.025    0.025    0.025 1136749821.py:1(summ)
#        1    0.000    0.000    0.025    0.025 <string>:1(<module>)
#        1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#cProfile.run('summ(10000000)')
#         4 function calls in 0.932 seconds
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.932    0.932    0.932    0.932 1136749821.py:1(summ)
#        1    0.000    0.000    0.932    0.932 <string>:1(<module>)
#        1    0.000    0.000    0.932    0.932 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Выводы:
#1) с увеличением n в 10 раз время работы функции увеличивается также примерно в 10 раз, т.е. #сложность алгоритма О(n);
#2) профилирование показывает, что каждый элемент функции вызывается только один раз, т.е. код #функции почти оптимален.
