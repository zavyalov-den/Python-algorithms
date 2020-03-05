# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.
from random import randint

SIZE = 10
ITEM_MIN = -100
ITEM_MAX = 100

max_negative = ITEM_MIN

arr = [randint(ITEM_MIN, ITEM_MAX) for _ in range(SIZE)]

for item in arr:
    if item < 0 and item > max_negative:
        max_negative = item


print(arr)
print(max_negative)
