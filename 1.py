import random


SIZE = 100
MIN_EL = -100
MAX_EL = 100
arr = [random.randint(MIN_EL, MAX_EL) for _ in range(SIZE)]


def bubble_sort(array):
    m = 0  # счетчик операций
    for i in range(len(array)):
        m += 1
        for j in range(len(array) - i - 1):
            m += 1
            if array[j] < array[j + 1]:
                m += 1
                array[j], array[j + 1] = array[j + 1], array[j]
    return m  # 7100-7800


def bubble_sort2(array):
    m = 0
    flag = False  # индикатор отсортированного массива, чтобы не пробегать по нему еще раз
    for i in range(len(array)):
        flag = False
        m += 1
        for j in range(len(array) - i - 1):
            m += 1
            if array[j] < array[j + 1]:
                m += 1
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break
    return m  # 7000-7700


print(arr)
print(bubble_sort2(arr))
print(arr)
