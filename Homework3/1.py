# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9
# Вариант 1

print('=' * 10, 'Вариант 1:', '=' * 10)

for i in range(START_DIV, END_DIV + 1):
    frequency = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    print(f'Числу {i} кратно {frequency} чисел')

# Вариант 2

print('=' * 10, 'Вариант 2:', '=' * 10)

frequency_ = [0] * (END_DIV - START_DIV + 1)  # [0] * 8
for i in range(START_NUM, END_NUM + 1):
    for j in range(START_DIV, END_DIV + 1):
        if i % j == 0:
            frequency_[j - START_DIV] += 1

for i, item in enumerate(frequency_, start=START_DIV):
    print(f'Числу {i} кратно {item} чисел')

# Вариант 3
print('=' * 10, 'Вариант 3:', '=' * 10)


def search_count(num):
    count_num = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % num == 0:
            count_num += 1
    return count_num


for i in range(2, 10):
    count = search_count(i)
    print(f'Числу {i} кратно {count} чисел')
