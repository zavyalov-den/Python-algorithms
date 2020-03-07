# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
ITEM_MIN = 0
ITEM_MAX = 100

arr_min = ITEM_MAX
arr_max = ITEM_MIN

arr = [random.randint(ITEM_MIN, ITEM_MAX) for _ in range(SIZE)]
print(arr)

for item in arr:
    if item < arr_min:
        arr_min = item
    if item > arr_max:
        arr_max = item

index_min = arr.index(arr_min)
index_max = arr.index(arr_max)

arr[index_min], arr[index_max] = arr[index_max], arr[index_min]

print(arr)

