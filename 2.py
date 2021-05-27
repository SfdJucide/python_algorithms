import timeit
import cProfile


def sieve(n):
    a = [i for i in range(n ** 2)]
    s = len(a)
    a[1] = 0
    m = 2
    for i in range(m, s):
        if a[i] != 0:
            m = i ** 2
            while m < s:
                a[m] = 0
                m += i
    prime_arr = [i for i in a if i != 0]
    return prime_arr[n - 1]


print(timeit.timeit('sieve(10)', number=1000, globals=globals()))  # 0.09123949999999999
print(timeit.timeit('sieve(20)', number=1000, globals=globals()))  # 0.3707595
print(timeit.timeit('sieve(40)', number=1000, globals=globals()))  # 1.6406611
print(timeit.timeit('sieve(100)', number=1000, globals=globals()))  # 10.5677375
# Функция квадратичная

print(cProfile.run('sieve(1000)'))
#         7 function calls in 1.096 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.081    0.081    0.081    0.081 2.py:16(<listcomp>)
#        1    0.871    0.871    1.077    1.077 2.py:5(sieve)
#        1    0.126    0.126    0.126    0.126 2.py:6(<listcomp>)
#        1    0.018    0.018    1.096    1.096 <string>:1(<module>)
#        1    0.000    0.000    1.096    1.096 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
