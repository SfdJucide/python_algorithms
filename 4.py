"""
https://drive.google.com/file/d/1BGc7Wc7NVNSI901FuQT36uWaG1Q2gqDJ/view?usp=sharing
"""


def row_sum(n):
    summ = 0
    if n == 1:
        return 2 ** 0
    elif n % 2 == 0:
        summ = row_sum(n - 1) - 2 ** (-(n - 1))
    else:
        summ = row_sum(n - 1) + 2 ** (-(n - 1))
    return summ


n = int(input("Введите число: "))
print(f"Сумма ряда из {n} элементов = {row_sum(n)}")  # ряд сходится к 2/3 :)
