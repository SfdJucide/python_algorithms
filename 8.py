"""
https://drive.google.com/file/d/1Am3x-K814MlZPynOwKx_LnkQrP1DRsiU/view?usp=sharing
начало
ввод года(year)
Если year без остатка делиться на 4
То Если year без остатка делиться на 100
   То Если year без остатка делиться на 400
      То вывод(год високосный)
      Иначе вывод(год невисокосный)
   Иначе вывод(год високосный)
Иначе вывод(год невисокосный)
конец
"""
year = int(input("Введите год "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Год високосный")
        else:
            print("Год невисокосный")
    else:
        print("Год високосный")
else:
    print("Год невисокосный")
