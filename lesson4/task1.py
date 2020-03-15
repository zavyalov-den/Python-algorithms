# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
import timeit
import cProfile


def variant_1(size, item_min, item_max):

    SIZE = size
    ITEM_MIN = item_min
    ITEM_MAX = item_max

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

    return result


def variant_2(size, item_min, item_max):

    result = 0

    arr = [randint(item_min, item_max) for _ in range(size)]

    el_min = arr[0]
    el_max = arr[0]

    index_min = 0
    index_max = 0

    for index, item in enumerate(arr):
        if item > el_max:
            index_max = index
        if item < el_min:
            index_min = index

    if index_max > index_min:
        arr2 = arr[index_min + 1:index_max]
    else:
        arr2 = arr[index_max + 1:index_min]

    for item in arr2:
        result += item

    return result


def variant_3(size, item_min, item_max):

    result = 0

    arr = [randint(item_min, item_max) for _ in range(size)]

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

    return result


print(timeit.timeit("variant_1(100, 0, 100)", number=100, globals=globals()))  # 0.015250599999999996
print(timeit.timeit("variant_1(10000, 0, 100)", number=100, globals=globals()))  # 1.2967249
print(timeit.timeit("variant_1(1000000, 0, 100)", number=100, globals=globals()))  # 132.6642942


print(timeit.timeit("variant_2(100, 0, 100)", number=100, globals=globals()))  # 0.01589709999998945
print(timeit.timeit("variant_2(10000, 0, 100)", number=100, globals=globals()))  # 1.4343360000000018
print(timeit.timeit("variant_2(1000000, 0, 100)", number=100, globals=globals()))  # 138.1116832


print(timeit.timeit("variant_3(100, 0, 100)", number=100, globals=globals()))  # 0.022694300000011935
print(timeit.timeit("variant_3(10000, 0, 100)", number=100, globals=globals()))  # 1.4161746000000335
print(timeit.timeit("variant_3(1000000, 0, 100)", number=100, globals=globals()))  # 140.06531010000003

cProfile.run("variant_3(10000, 0, 100)")  # 10000    0.007    0.000    0.010    0.000 random.py:224(_randbelow)
cProfile.run("variant_3(100000, 0, 100)")  # 100000    0.068    0.000    0.096    0.000 random.py:224(_randbelow)
cProfile.run("variant_3(1000000, 0, 100)")  # 1000000    0.579    0.000    0.816    0.000 random.py:224(_randbelow)


# Данный труд затевался как проверка серьезности моих "ошибок" в решении данной задачи (и других аналогичных). Вариант 1 - как было.
# Вариант 2 имеет ряд улучшених (избавился от индексов и упростил код), 3й вариант еще "чище", легче читается и избавлен от использования
# нескольких лишних имен.

# По результату. Выбор задачи был не самым лучшим. Самое грустное - то, что самым затратным действием является генерация списка =)
# Все 3 варианта показали полную линейность с минимальным различием в скорости выполнения.
# Так что оптимизация в 1ю очередь повлияла на "чистоту" кода, что есть огромный плюс. При работе с большими объемами данных также должен быть
# небольшой выигрыш по используемому объему памяти.
