'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанные программы в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программ или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
'''

import sys


def sum_memory(objects):
    '''
    Принимает на вход набор объектов, т.е. "словарь"
    '''
    sum_mem = 0
    unique_id = set()
    for key, value in objects.items():
        if key.startswith('__'):
            # проверяем наличие логических или dunder ('магических') методов
            continue
        elif hasattr(value, '__call__'):
            # убираем функции
            continue
        elif hasattr(value, '__loader__'):
            # убираем модули
            continue
        elif id(value) in unique_id:
            # убираем объекты (переменные), которые уже попали в сумму
            continue
        else:
            # if hasattr(obj, '__iter__'):
            #     if hasattr(obj, 'items'):
            #         for key, value in obj.items():
            #             self._add(key)
            #             self._add(value)
            #     elif not isinstance(obj, str):
            #         for item in obj:
            #             self._add(item)
            unique_id.add(id(value))
            sum_mem += sys.getsizeof(value)
            print(f'переменная {key} класса {type(value)} хранит {value} '
                  f'и занимает {sys.getsizeof(value)} байт')

    return sum_mem
# Версия Python 3.7 Windows 10 / 64-разрядная ОС