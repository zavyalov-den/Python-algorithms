# https://drive.google.com/file/d/1YqHZQusscl6dTxgF2KATGuihlMFskHe6/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = input('Введите трехзначное число: ')

x, y, z = n
x, y, z = int(x), int(y), int(z)

a = x * y * z
b = x + y + z

print(f'произведение {a=} \nсумма {b=}')
