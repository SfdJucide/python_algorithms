import random


m = random.randint(3, 5)
SIZE = 2 * m + 1
MIN_EL = 0
MAX_EL = 10
arr = [random.randint(MIN_EL, MAX_EL) for _ in range(SIZE)]
print(arr)


def median(a, k):
    if len(a) == 1:
        return a[0]

    pivot = random.choice(a)

    left = [el for el in a if el < pivot]
    right = [el for el in a if el > pivot]
    mid = [el for el in a if el == pivot]

    if k < len(left):
        return median(left, k)
    elif k < len(left) + len(mid):
        return mid[0]
    else:
        return median(right, k - len(left) - len(mid))


print(f'медиана равна - {median(arr, len(arr) / 2)}')
