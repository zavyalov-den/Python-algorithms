# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;

# ● написать 3 варианта кода (один у вас уже есть);

# ● проанализировать 3 варианта и выбрать оптимальный;

# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

# ● написать общий вывод: какой из трёх вариантов лучше и почему.

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

el_min = ITEM_MAX
el_max = ITEM_MIN

result = 0

arr = [randint(ITEM_MIN, ITEM_MAX) for _ in range(SIZE)]

for item in arr:
    if item > el_max:
        el_max = item
    if item < el_min:
        el_min = item

    # print(arr)

index_min = arr.index(el_min)
index_max = arr.index(el_max)

if index_max > index_min:
    arr2 = arr[index_min + 1:index_max]
else:
    arr2 = arr[index_max + 1:index_min]

for item in arr2:
    result += item

all_vars = [SIZE, ITEM_MAX, ITEM_MIN, el_max, el_min, result, arr, index_max, index_min, arr2, item]

for var in all_vars:
    getsize(var)


print(f'всего использовано {count} переменных, общим размером {total} байт. ')
