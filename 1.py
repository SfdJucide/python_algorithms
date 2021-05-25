START = 2
STOP = 100
arr = [0] * 8    # массив для счетчиков кратности
for num in range(START, STOP):
    if num % 2 == 0:
        arr[0] += 1
    if num % 3 == 0:
        arr[1] += 1
    if num % 4 == 0:
        arr[2] += 1
    if num % 5 == 0:
        arr[3] += 1
    if num % 6 == 0:
        arr[4] += 1
    if num % 7 == 0:
        arr[5] += 1
    if num % 8 == 0:
        arr[6] += 1
    if num % 9 == 0:
        arr[7] += 1

for number, count in enumerate(arr):
    print(f'{count} чисел кратны {number + 2}')
