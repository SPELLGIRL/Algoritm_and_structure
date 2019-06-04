#
# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанные программы в рамках первых трех уроков. Проанализировать
# результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программ или несколько
# вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
# комментариев к коду. Также укажите в комментариях версию Python
# и разрядность вашей ОС.
#

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

from sum_memory_2 import sum_memory

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0
for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i
print(f'Min = {array[idx_min]} в ячейке {idx_min};\n'
      f'Max = {array[idx_max]} в ячейке {idx_max}')

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

print(locals())  # функция, которая возвращает словарь, содержащий ВСЕ локальные объекты
print('*' * 50)
print(sum_memory(locals()))
