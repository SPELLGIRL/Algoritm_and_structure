"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def sum_natural(n):
    assert n < 999, 'Слишком большое число'
    if n == 1:
        return n
    sum_n = n + sum_natural(n - 1)
    return sum_n


n = int(input('Введите любое натуральное число: '))


left = sum_natural(n)
right = n * (n + 1) // 2

print(f'1 + 2 + ... + n = {left}')
print(f'n(n + 1)/2 = {right}')
print(f'Сравнив результат получаем: {left == right}')
