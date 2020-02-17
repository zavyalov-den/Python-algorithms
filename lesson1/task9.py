# https://drive.google.com/file/d/1hKpk4Vn4Ns70ty3Ugdl2Blgk8syb8C86/view?usp=sharing
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

n = input('Введите 3 разных числа через пробел: ')

a, b, c = n.split()
a, b, c = int(a), int(b), int(c)

if a > b and a > c:
    if b > c:
        print(f'{b=}')
    else: 
        print(f'{c=}')
else:
    if a > b or c > c:
        print(f'{a=}')
    else:
        if b > c:
            print(f'{c=}')
        else: 
            print(f'{b=}')



