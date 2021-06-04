"""
Определить, какое число в массиве встречается чаще всего.
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
"""


import sys
import random
from collections import Counter, defaultdict


program_memory = []


def memory(*args):
    global total_memory
    for obj in args:
        print(f"Размер объекта {obj} - {(sys.getsizeof(obj))} байт")
        total_memory += sys.getsizeof(obj)
        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    memory(key)
                    memory(value)
            elif not isinstance(obj, str):
                for el in obj:
                    memory(el)


# 1 вариант
SIZE = 10
MIN_EL = 0
MAX_EL = 20
arr = [random.randint(MIN_EL, MAX_EL) for _ in range(SIZE)]
print(arr)

if len(arr) == len(set(arr)):
    print('Все элементы уникальны')

    # testing
    print('*' * 50)
    total_memory = 0
    memory(SIZE, MIN_EL, MAX_EL, arr)
    print(f'\nВсего памяти использовано - {total_memory} байт')
    program_memory.append([total_memory, 1])
    print('*' * 50)
else:
    counter = {}
    count = 1
    num = None
    for item in arr:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > count:
            count = counter[item]
            num = item

    print(f'Число {num} встречется {count} раз\n')


# testing
    print('*' * 50)
    total_memory = 0
    memory(SIZE, MIN_EL, MAX_EL, arr, counter, count, num)
    print(f'\nВсего памяти использовано - {total_memory} байт')
    program_memory.append([total_memory, 1])
    print('*' * 50)


# 2 вариант
SIZE = 10
MIN_EL = 0
MAX_EL = 20
arr = [random.randint(MIN_EL, MAX_EL) for _ in range(SIZE)]
print(arr)

if len(arr) == len(set(arr)):
    print('Все элементы уникальны')

    # testing
    print('*' * 50)
    total_memory = 0
    memory(SIZE, MIN_EL, MAX_EL, arr)
    print(f'\nВсего памяти использовано - {total_memory} байт')
    program_memory.append([total_memory, 2])
    print('*' * 50)
else:
    counter = Counter(arr)
    print(f'Число {counter.most_common(1)[0][0]} встречется {counter.most_common(1)[0][1]} раз')


# testing
    print('*' * 50)
    total_memory = 0
    memory(SIZE, MIN_EL, MAX_EL, arr, counter)
    print(f'\nВсего памяти использовано - {total_memory} байт')
    program_memory.append([total_memory, 2])
    print('*' * 50)


# 3 вариант
SIZE = 10
MIN_EL = 0
MAX_EL = 20
arr = [random.randint(MIN_EL, MAX_EL) for _ in range(SIZE)]
print(arr)

if len(arr) == len(set(arr)):
    print('Все элементы уникальны')

    # testing
    print('*' * 50)
    total_memory = 0
    memory(SIZE, MIN_EL, MAX_EL, arr)
    print(f'\nВсего памяти использовано - {total_memory} байт')
    program_memory.append([total_memory, 3])
    print('*' * 50)
else:
    counter = defaultdict(int)
    for num in arr:
        counter[num] += 1

    max_c = 0
    new_num = 0
    for num, count in counter.items():
        if count > max_c:
            max_c = count
            new_num = num

    print(f'Число {new_num} встречется {max_c} раз')


# testing
    print('*' * 50)
    total_memory = 0
    memory(SIZE, MIN_EL, MAX_EL, arr, counter, max_c, new_num)
    print(f'\nВсего памяти использовано - {total_memory} байт')
    program_memory.append([total_memory, 3])
    print('*' * 50)


print(program_memory)
res = min([program_memory[i][0] for i in range(len(program_memory))])
for lst in program_memory:
    if res in lst:
        print(f"По затреченной памяти вариант программы {lst[1]} оказался более эффективным")

# в большинстве случаев 1 и 2 вариант самые эффективные
