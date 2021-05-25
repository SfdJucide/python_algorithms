import random
SIZE = 10
MIN_EL = 0
MAX_EL = 100
arr = [random.randint(MIN_EL, MAX_EL) for _ in range(SIZE)]
print(arr)

min = arr[0]
max = arr[0]
min_idx = 0
max_idx = 0
for i, el in enumerate(arr):
    if el < min:
        min = el
        min_idx = i
    if el > max:
        max = el
        max_idx = i

arr[min_idx] = max
arr[max_idx] = min
print(arr)
