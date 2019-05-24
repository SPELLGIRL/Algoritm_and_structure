"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

N = 5
M = 4
matrix = []
for i in range(N):
    row = []
    sum_ = 0

    for j in range(M - 1):
        num = int(input(f'{i}-я строка, {j}-й элемент : '))
        sum_ += num
        row.append(num)

    row.append(sum_)
    matrix.append(row)

print('=' * 10, 'Получена матрица:', '=' * 10)
for line in matrix:
    print(line)