# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 99

MULTIPLIER_MIN = 2
MULTIPLIER_MAX = 9

result = {key: 0 for key in range(MULTIPLIER_MIN, MULTIPLIER_MAX + 1)}
arr = [item for item in range(MIN_ITEM, MAX_ITEM + 1)]

for item in arr:
    for key in result:
        if item % key == 0:
            result[key] += 1


for key in result:
    print(f' кратных числу {key}: {result[key]}')
