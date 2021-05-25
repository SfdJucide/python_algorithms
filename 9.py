import random
SIZE_M = 3
SIZE_N = 3
MIN_EL = 0
MAX_EL = 100
matrix = [[random.randint(MIN_EL, MAX_EL) for _ in range(SIZE_M)] for _ in range(SIZE_N)]
print(*matrix, sep='\n')

min_arr = [MAX_EL] * len(matrix[0])
i = 0
for i in range(len(matrix[0])):
    for line in matrix:
        if line[i] < min_arr[i]:
            min_arr[i] = line[i]
            continue
    i += 1
print(min_arr)

max_col_el = min_arr[0]
for el in min_arr:
    if el > max_col_el:
        max_col_el = el

print(f"Максимальный элемент среди минимальных элементов столбцов матрицы - {max_col_el}")
