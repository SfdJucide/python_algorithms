"""
https://drive.google.com/file/d/1ijOVVInH3oq9knw2NUZJFKVQLFVbUFA5/view?usp=sharing
"""


def reverse_print(n):
    if n < 10:
        return n
    else:
        reverse_n = str(n % 10) + str(reverse_print(n // 10))
        return int(reverse_n)


n = int(input("Введите число: "))
print(reverse_print(n))
