# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25,
# -0.125,… Количество элементов (n) вводится с клавиатуры.

# https://drive.google.com/file/d/1Mc9wfBDO2I4HCVYLGVzmc97R3GbD-U88/view?usp=sharing


def my_sum(n):
    if n == 1:
        return 1
    else:
        return (-0.5) ** (n - 1) + my_sum(n - 1)


n = int(input('Введите количество элементов n: '))
result = my_sum(n)

print(result)
