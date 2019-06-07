"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random


def merger_sort(arr):
    """
    Функция сортировки слиянием, проверка по половине массива
    :param arr: массив вещественных чисел
    :return: отсортированный массив в порядке возрастания
    """

    if len(arr) <= 1:
        return arr

    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    # Необязательная часть, без нее также работает, эта часть ускоряет процесс

    left = merger_sort(arr[:len(arr) // 2])
    right = merger_sort(arr[len(arr) // 2:])
    i, j = 0, 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            arr[i + j] = left[i]
            i += 1
        else:
            arr[i + j] = right[j]
            j += 1

    while len(left) > i:
        arr[i + j] = left[i]
        i += 1

    while len(right) > j:
        arr[i + j] = right[j]
        j += 1

    return arr


SIZE = 10
LIMIT = 50
array = [round(random.uniform(0, LIMIT), 2) for _ in range(SIZE)]
print(f'Первоначальный вещественный массив: \n{array}')
merger_sort(array)
print(f'Полученный отсортированный массив:\n{array}')
