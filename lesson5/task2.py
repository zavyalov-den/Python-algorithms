# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

digits = deque(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'])

a = deque(input('Введите 1е шестнадцатиричное число: ').upper())
b = deque(input('Введите 2е шестнадцатиричное число: ').upper())

a.reverse()
b.reverse()
s = deque([])
# m = deque([])

if len(a) < len(b):
    a, b = b, a

extra = 0
for index, num in enumerate(a):
    if index < len(b):
        arr = digits.copy()
        turn = digits.index(num) + digits.index(b[index]) + extra
        extra = turn // len(digits)

        arr.rotate(-turn)
        s.appendleft(arr[0])

    else:
        s.appendleft(num)

if extra > 0:
    arr = digits.copy()
    s.appendleft(arr[extra])


print(f'Сумма {s}')
