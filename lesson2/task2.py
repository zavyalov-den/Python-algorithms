# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и
# 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1Mc9wfBDO2I4HCVYLGVzmc97R3GbD-U88/view?usp=sharing

n = int(input('Введите целое число: '))

even = 0
odd = 0

while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

    n = n // 10

print(f'even: {even} \n odd: {odd}')
