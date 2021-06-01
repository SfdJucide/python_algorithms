import collections as cll

first = input("Введите первое число в шестнадцатеричной системе счисления > ")
second = input("Введите первое число в шестнадцатеричной системе счисления > ")


def sum_in_sixteen(a, b):
    to_ten = {'0': 0, '1': 1,
              '2': 2, '3': 3,
              '4': 4, '5': 5,
              '6': 6, '7': 7,
              '8': 8, '9': 9,
              'A': 10, 'B': 11,
              'C': 12, 'D': 13,
              'E': 14, 'F': 15}

    from_ten = {10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F'}

    num1 = cll.deque()
    for num in a:
        num1.append(num)

    num2 = cll.deque()
    for num in b:
        num2.append(num)

    while len(num1) != len(num2):
        if len(num1) > len(num2):
            num2.appendleft('0')
        else:
            num1.appendleft('0')

    res = cll.deque()
    print(num1)
    print(num2)

    for i in range(len(num1) - 1, -1, -1):
        res.appendleft(to_ten.get(num1[i]) + to_ten.get(num2[i]))

    res.appendleft(0)
    for i in range(len(res) - 1, -1, -1):
        if 10 <= res[i] <= 15:
            res[i] = from_ten.get(res[i])
        elif res[i] > 15:
            res[i] -= 16
            res[i - 1] += 1
            if res[i] >= 10:
                res[i] = from_ten.get(res[i])
            else:
                res[i] = str(res[i])
        else:
            res[i] = str(res[i])
        print(res)
    for el in res:
        print(el, sep='', end='')


sum_in_sixteen(first, second)
