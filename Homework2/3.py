"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

# вариант 1
num = int(input('Введите целое число: '))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(result)

# вариант 2
num = input('Введите целое число: ')
result = ''
for i in num:
    result = i + result
print(result)

# вариант 3
num = input('Введите целое число: ')
result = num[::-1]
print(result)

# Вариант 4 (рекурсия)
num = input('Введите целое число: ')


def recursion(n):
    n = int(n)
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + str(recursion(n // 10))


print(recursion(num))
