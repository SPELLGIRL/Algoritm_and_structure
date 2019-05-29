"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple, deque

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятия {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)

    all_companies.add(comp)
    total_profit += profit

average = total_profit / num

print(f'\nСредняя прибыль = {average}')

# вариант 1
print(f'\nПредприятия с прибылью выше среднего:')
for comp in all_companies:
    if comp.profit > average:
        print(f'Компания {comp.name} заработала {comp.profit}')
        # print(comp.quarters[0])   # так можно получить доступ к нужной четверти.

print(f'\nПредприятя с прибылью ниже среднего:')
for comp in all_companies:
    if comp.profit < average:
        print(f'Компания {comp.name} заработала {comp.profit}')

# вывод результата с использованием очереди - вариант 2
print('*' * 50)

sort_comp = deque([None])
for comp in all_companies:
    if comp.profit > average:
        sort_comp.append(comp)
    elif comp.profit < average:
        sort_comp.appendleft(comp)

text = 'меньше'
for comp in sort_comp:
    if comp is None:
        text = 'больше'
    else:
        print(f'Компания {comp.name} заработала {text}, чем средняя прибыль - {comp.profit}')

'''# цикл вместо дублирования 4 строчек кода
from collections import namedtuple

all_comp = []
Comp = namedtuple('Comp', 'name, p1, p2, p3, p4, total')
num = int(input('num = '))
for i in range(num):
    name = input('name = ')
    spam = []
    for j in range(1, 5):
        spam.append(int(input(f'{j} = ')))
    all_comp.append(Comp(name, *spam, sum(spam)))

print(all_comp)
'''
