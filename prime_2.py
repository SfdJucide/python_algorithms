import timeit
import cProfile


def prime(n):
    number = 1
    prime_ = 2
    while number < n:
        prime_ += 1
        for i in range(2, prime_ // 2 + 1):
            if prime_ % i == 0:
                break
        else:
            number += 1
    return prime_


print(prime(45))

print(timeit.timeit('prime(10)', number=1000, globals=globals()))  # 0.03904199999999999
print(timeit.timeit('prime(20)', number=1000, globals=globals()))  # 0.11703949999999999
print(timeit.timeit('prime(40)', number=1000, globals=globals()))  # 0.38707579999999997
print(timeit.timeit('prime(100)', number=1000, globals=globals()))  # 2.2270273
# Функция квадратичная, но быстрее первого варианта в 3-4 раза

print(cProfile.run('prime(1000)'))

#         4 function calls in 0.335 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.335    0.335 <string>:1(<module>)
#        1    0.335    0.335    0.335    0.335 prime_2.py:5(prime)
#        1    0.000    0.000    0.335    0.335 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
