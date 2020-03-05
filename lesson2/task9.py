# 9. Среди натуральных чисел, которые были введены, найти наибольшее
# по сумме цифр. Вывести на экран это число и сумму его цифр.

# https://drive.google.com/file/d/1Mc9wfBDO2I4HCVYLGVzmc97R3GbD-U88/view?usp=sharing


def sumdigits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sumdigits(n // 10)


number = 0
max_sum = 0

while True:
    num = int(input('Введите натуральное число или введите 0 для выхода: '))
    if num == 0:
        break
    elif sumdigits(num) > max_sum:
        number = num
        max_sum = sumdigits(num)

print(f'Число с максимальной суммой цифр: {number} \nСумма его цифр: {max_sum}')
