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


class SumMemory:

    def __init__(self):
        """
        _sum_memory - общее количество занятой памяти
        _types - словарь вида {'type': [count, size]}
        """
        self._sum_memory = 0
        self._types = {}

    def extend(self, *args):
        '''
        Принимает неограниченное число элементов, перебирая все объекты в цикле
        вызывает встроенный метод _add, который занимается суммированием.
        :param args: элемент (может быть неограниченное количество)
        '''
        for obj in args:
            self._add(obj)

    def _add(self, obj):
        '''
        Получает по очереди каждый объект, во временную переменную spam сохраняет размер данного объекта.
        В переменную eggs сохраняет тип данного объекта, увеличивает главную переменную на размер spam
        :param obj: принимает на вход объект
        Переменная _sum_memory служит для подсчета общего количества затраченной памяти.
        '''
        spam = sys.getsizeof(obj)
        eggs = str(type(obj))
        self._sum_memory += spam
        if eggs in self._types:  # расширение функционала
            self._types[eggs][0] += 1
            self._types[eggs][1] += spam
        else:
            self._types[eggs] = [1] * 2
            self._types[eggs][1] = spam

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    self._add(key)
                    self._add(value)
            elif not isinstance(obj, str):
                for item in obj:
                    self._add(item)

    def print_sum(self):
        print(f'Переменные заняли в сумме {self._sum_memory} байт')
        for key, value in self._types.items():
            print(f'Объекты класса {key} в количестве {value[0]} заняли {value[1]} байт')

# Версия Python 3.7 Windows 10 / 64-разрядная ОС