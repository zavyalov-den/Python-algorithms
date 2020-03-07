# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

SIZE = 10
ITEM_MIN = 0
ITEM_MAX = 100

el_min = ITEM_MAX
el_max = ITEM_MIN

result = 0

arr = [randint(ITEM_MIN, ITEM_MAX) for _ in range(SIZE)]

for item in arr:
    if item > el_max:
        el_max = item
    if item < el_min:
        el_min = item

print(arr)

index_min = arr.index(el_min)
index_max = arr.index(el_max)

if index_max > index_min:
    arr2 = arr[index_min + 1:index_max]
else:
    arr2 = arr[index_max + 1:index_min]

for item in arr2:
    result += item

print(arr2)
print(result)
