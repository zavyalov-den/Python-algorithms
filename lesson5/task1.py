# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

n = int(input('Введите количество предприятий: '))

# Будем складывать деньги
data = defaultdict(int)
profit = 0

for _ in range(n):
    name = input('Введите название предприятия: ')
    for x in range(4):
        data[name] += int(input(f'Для предприятия {name} введите прибыль за кварта №{x + 1}: '))

    profit += data[name]

avg = profit / n

result = defaultdict(list)

for company in data:
    if data[company] > avg:
        result['above'].append(company)
    elif data[company] < avg:
        result['below'].append(company)
    else:
        result['average'].append(company)

print('С прибылью выше среденего: ')
for name in result['above']:
    print(name)

print('С прибылью ниже среденего: ')
for name in result['below']:
    print(name)

# if len(result['average']) > 0:
if 'average' in result:
    print('Средненькие компании: ')

    for name in result['average']:
        print(name)
