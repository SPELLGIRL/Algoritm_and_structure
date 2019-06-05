"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def bubble_sort(arr, reverse=False):
    """
    Функция сортировки массива по возрастанию.
    :param arr: принимает на вход массив случайных целых чисел
    :param reverse: Порядок сортировки, прямой False, обратный - True
    """
    sign = int(reverse) * 2 - 1
    n = 1

    while n < len(arr):
        is_sorted = True
        for i in range(len(arr) - n):
            if arr[i] * sign < arr[i + 1] * sign:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False

        if is_sorted:
            break

        n += 1


SIZE = 20
LIMIT = 100
array = [random.randrange(-LIMIT, LIMIT) for _ in range(SIZE)]
# Выбран метод ranrange  по причине условия, включая первое число и не включая последнее
print(f'Первоначальный массив:\n {array}')
bubble_sort(array, reverse=True)
print(f'Получен отсортированный массив: \n{array}')
