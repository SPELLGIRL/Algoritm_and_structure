# 4.	Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 20
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE / 2) for _ in range(SIZE)]
print(f'Случайный массив чисел: {array}')

# вариант 1
print('=' * 10, 'Вариант 1:', '=' * 10)

num = array[0]
frequency = 1
for i in range(len(array)):
    spam = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            spam += 1
    if spam > frequency:
        frequency = spam
        num = array[i]

if frequency > 1:
    print(f'Число {num} встречется {frequency} раз(а)')
else:
    print('Все элементы уникальны')

# ваниант 2
print('=' * 10, 'Вариант 2:', '=' * 10)

counter = {}
count = 1
num = None
for item in array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1
    if counter[item] > count:
        count = counter[item]
        num = item

if num is not None:
    print(f'Число {num} встречется {count} раз(а)')
else:
    print('Все элементы уникальны')
