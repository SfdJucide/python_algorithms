import timeit
import cProfile

"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def row_sum1(n):  # Линейная функция
    sum_ = 0
    if n == 1:
        return 2 ** 0
    elif n % 2 == 0:
        sum_ = row_sum1(n - 1) - 2 ** (-(n - 1))
    else:
        sum_ = row_sum1(n - 1) + 2 ** (-(n - 1))
    return sum_


def row_sum2(n):  # Линейная функция
    sum_ = 0
    for i in range(n):
        if i % 2 == 0:
            sum_ += 2 ** (-i)
        else:
            sum_ -= 2 ** (-i)
    return sum_


def row_sum3(num, start=1.0, step=-0.5):  # Линейная функция при N < 56, при N > 55 функция константа
    if num == 1:
        return start
    if num > 55:
        return 2/3
    return start + row_sum3(num - 1, start * step)


print(timeit.timeit('row_sum1(10)', number=1000, globals=globals()))  # 0.011859599999999998
print(timeit.timeit('row_sum1(20)', number=1000, globals=globals()))  # 0.027325000000000002
print(timeit.timeit('row_sum1(40)', number=1000, globals=globals()))  # 0.050729600000000014
print(timeit.timeit('row_sum1(80)', number=1000, globals=globals()))  # 0.10583900000000002
print(timeit.timeit('row_sum1(160)', number=1000, globals=globals()))  # 0.1935929
print()
print(timeit.timeit('row_sum2(10)', number=1000, globals=globals()))  # 0.009155899999999995
print(timeit.timeit('row_sum2(20)', number=1000, globals=globals()))  # 0.017172200000000026
print(timeit.timeit('row_sum2(40)', number=1000, globals=globals()))  # 0.028762000000000065
print(timeit.timeit('row_sum2(80)', number=1000, globals=globals()))  # 0.05828960000000005
print(timeit.timeit('row_sum2(160)', number=1000, globals=globals()))  # 0.13303890000000007
print()
print(timeit.timeit('row_sum3(10)', number=1000, globals=globals()))  # 0.004731400000000052
print(timeit.timeit('row_sum3(20)', number=1000, globals=globals()))  # 0.011062500000000086
print(timeit.timeit('row_sum3(40)', number=1000, globals=globals()))  # 0.023162000000000016
print(timeit.timeit('row_sum3(80)', number=1000, globals=globals()))  # 0.0003870999999999736
print(timeit.timeit('row_sum3(160)', number=1000, globals=globals()))  # 0.00043949999999992606

print(cProfile.run('row_sum1(900)'))

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    900/1    0.003    0.000    0.003    0.003 1.py:10(row_sum1)
#        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(cProfile.run('row_sum2(100000)'))

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.101    0.101    0.101    0.101 1.py:21(row_sum2)
#        1    0.000    0.000    0.101    0.101 <string>:1(<module>)
#        1    0.000    0.000    0.101    0.101 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(cProfile.run('row_sum3(100000**10)'))

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 1.py:31(row_sum3)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
