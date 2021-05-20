"""
https://drive.google.com/file/d/1D7RZg6Vf9HSr6CC-TjNGVtmoWRx_2DUC/view?usp=sharing
"""

n = int(input("Введите число: "))
even = 0
odd = 0
for i in range(len(str(n))):
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10

print(f"Четных цифр: {even}")
print(f"Нечетных цифр: {odd}")
