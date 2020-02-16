# https://drive.google.com/file/d/1SZnVTGW1OLGSNtLSgUKYKQDzssslpulw/view?usp=sharing
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

y = int(input("Введите год: "))

if y % 400 == 0: 
    print('Год високосный')
else:
    if y % 100 == 0: 
        print('Год невисокосный')
    elif y % 4 == 0:
        print('Год високосный')
    else:
        print('Год невисокосный')