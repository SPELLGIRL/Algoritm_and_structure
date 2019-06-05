"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

import random

print("=" * 10, "Вариант № 1:", "=" * 10)


def partition(arr, pivot):
    """
    Функция разбивает массив на три части меньше
    опорного, больше опорного и равный опорному
    :param arr: массив чисел
    :param pivot: произвольное число, которое и будет разбивать массив
    :return: три массива чисел
    """
    small = []
    equality = []
    big = []
    for item in arr:
        if item < pivot:
            small.append(item)
        elif item > pivot:
            big.append(item)
        else:
            equality.append(item)
    return small, equality, big


def top_key(arr, key):
    """
    Функция поиска позиции медианы в массиве
    :param arr: массив чисел
    :param key: значение, вычисляемое функцией
    :return: значение ключа в зависимости от условия
    """
    pivot = arr[random.randrange(len(arr))]
    left, middle, right = partition(arr, pivot)

    if len(left) == key:
        return left
    if len(left) < key <= len(left) + len(middle):
        return middle
    if len(left) > key:
        return top_key(left, key)
    return top_key(right, key - len(left) - len(middle))


def median(arr):
    """
    Функция расчета медианы
    :param arr: массив чисел
    :return: значение медианы
    """
    result_list = top_key(arr, len(arr) // 2 + 1)
    return max(result_list)


m = random.randint(1, 5)
LIMIT = 100
array = [random.randrange(0, LIMIT) for _ in range(2 * m + 1)]
print(f'Первоначальный случайный массив: \n{array}')
print(f'Медиана  = {median(array)}')
print(f'Новый, отсортированный массив: \n{sorted(array)}')

print("=" * 10, "Вариант № 2:", "=" * 10)

import statistics

array = [random.randrange(0, LIMIT) for _ in range(2 * m + 1)]
print(f'Массив случайных чисел: \n{array}')
print(f'Median = {statistics.median(array)}')
print(f'Отсортированный массив: \n{sorted(array)}')
