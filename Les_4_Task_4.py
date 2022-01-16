#!/usr/bin/env python
# coding: utf-8

# # Решето Эратосфена

# ## Нахождение i-го по счёту простого числа с помощью алгоритма "решето Эратосфена"



import timeit
import cProfile



def sieve(a):
    
    result = []
    n = 20
    def help_f(n):
        _sieve = [i for i in range(n)]
        _sieve[1] = 0

        for i in range(2,n):

            if _sieve[i] != 0:
                j = i * 2

                while j < n:
                    _sieve[j] = 0
                    j += i

        _result = [i for i in _sieve if i != 0]
        
        return _result
    
    result.extend(help_f(n))
    
    while True:
        if len(result) < a:
            n += a * 10
            help_f(n)
            result.clear()
            result.extend(help_f(n))
        else:
            break
    
    return result[a]
    

#python3 -m timeit -n 1000 -s "import Les_4_Task_4" "Les_4_Task_4.sieve(100)"
#1000 loops, best of 5: 295 usec per loop

#python3 -m timeit -n 1000 -s "import Les_4_Task_4" "Les_4_Task_4.sieve(1000)"
#1000 loops, best of 5: 3.23 msec per loop

#python3 -m timeit -n 1000 -s "import Les_4_Task_4" "Les_4_Task_4.sieve(10000)"
#1000 loops, best of 5: 105 msec per loop


#cProfile.run('sieve(1000)')
#         18 function calls in 0.012 seconds
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        3    0.010    0.003    0.012    0.004 1012695584.py:5(help_f)

#cProfile.run('sieve(10000)')
#         27 function calls in 0.152 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        5    0.125    0.025    0.150    0.030 1012695584.py:5(help_f)

#cProfile.run('sieve(100000)')
#         27 function calls in 1.406 seconds
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        5    1.191    0.238    1.380    0.276 1012695584.py:5(help_f)


#Выводы:
#1) с увеличением n в 10 раз время работы функции увеличивается не пропорционально: в области низких #n линейно, т.е. О(n); далее в области высоких сложность алгоритма изменяется на О(n^2);
#2) профилирование показывает, что с увеличением n число вызовов внутренней функции help_f() также #растет, но до некоторого предела, затем выходит на плато.
