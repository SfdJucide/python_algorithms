"""
https://drive.google.com/file/d/1yEvvgkto2l_Ajx-_AZ6pLSjIoQokh0Uf/view?usp=sharing
"""


def proof(n):
    if n == 1:
        return n
    else:
        row_sum = proof(n - 1) + n
    return row_sum


n = int(input("Введите число: "))
a = proof(n)
if a == ((n * (n + 1)) / 2):
    print(f'Доказано равенство 1+2+...+n = n(n+1)/2 для числа {n}')
else:
    print(f'Равенство 1+2+...+n = n(n+1)/2 для числа {n} оказалось ложным!')
