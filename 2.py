import random
SIZE = 10
MIN_EL = 0
MAX_EL = 100
first_arr = [random.randint(MIN_EL, MAX_EL) for _ in range(SIZE)]
print(first_arr)
second_arr = [idx for idx, num in enumerate(first_arr) if num % 2 == 0]
print(second_arr)
