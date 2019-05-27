# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Случайный массив: {array}')

# вариант 1
print('=' * 10, 'Вариант № 1:', '=' * 10)

i = 0
index = -1
while i < len(array):  # или for i in range(len(array)):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

if index != -1:
    print(f'Максимальное отрицательное число {array[index]} '
          f'находится в ячейке {index}')

# вариант 2
print('=' * 10, 'Вариант № 2:', '=' * 10)

num = float('-inf')
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i

if num != float('-inf'):
    print(f'Максимальное отрицательное число {num} '
          f'находится в ячейке {index}')
