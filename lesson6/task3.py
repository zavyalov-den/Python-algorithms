from random import randint
from sys import getsizeof


total = 0
count = 0


def getsize(var):
    global total, count
    size = getsizeof(var)
    total += size
    count += 1

    if hasattr(var, '__iter__'):
        if hasattr(var, 'items'):
            for key, value in var.items():
                getsize(key)
                getsize(value)
        elif not isinstance(var, str):
            for item in var:
                getsize(item)


SIZE = 100
ITEM_MIN = 0
ITEM_MAX = 100


result = 0

arr = [randint(ITEM_MIN, ITEM_MAX) for _ in range(SIZE)]

el_min = arr[0]
el_max = arr[0]

index_min = 0
index_max = 0

for index, item in enumerate(arr):
    if item > el_max:
        index_max = index
    if item < el_min:
        index_min = index

if index_min > index_max:
    index_max, index_min = index_min, index_max

for i in range(index_min + 1, index_max):
    result += arr[i]


all_vars = [SIZE, ITEM_MAX, ITEM_MIN, result, arr, el_max, el_min, index_max, index_min, index, item]

for var in all_vars:
    getsize(var)

try:
    getsize(i)
except NameError:
    pass

print(f'всего использовано {count} переменных, общим размером {total} байт. ')


# Результаты замеров разнятся из-за использования randint и использования среза, но порядок примерно следующий:
# пример 1 и 2: всего использовано 181 переменных, общим размером 6528 байт.
# пример 3: всего использовано 112 переменных, общим размером 4016 байт.
# 3й вариант существенно эффективнее засчет отказа от использования промежуточного массива, созданного при помощи среза.
# в результате и количество переменных и объем занятой памяти снизился.
# Версия питона: 3.7.3 64-bit
