import random
MAX_EL = 50
SIZE = 35
arr = [random.random() * 50 for _ in range(SIZE)]


def merge_sort(array):
    if len(array) > 1:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]

        merge_sort(left)
        merge_sort(right)

        k, i, j = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


print(arr)
merge_sort(arr)
print(arr)
