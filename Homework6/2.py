# 2. Создать пользовательский класс данных (или использовать)
# реализованный в курсе Python.Основы. Реализовать
# и обычным способом. Проверить отображение словаря атрибуты. Сравнить
# классов.

from pympler import asizeof
from sys import getsizeof


class Human:
    def __init__(self, firstname: str, lastname: str, age: int, position: str):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.position = position


class HumanSlots:
    __slots__ = ('firstname', 'lastname', 'age', 'position')

    def __init__(self, firstname: str, lastname: str, age: int, position: str):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.position = position


# Создаем два объекта разных классов с одинаковыми данными:

Peter = Human('Peter', 'Pettigrew', 38, 'tail')
Peter_slots = HumanSlots('Peter', 'Pettigrew', 38, 'tail')

# Вызовем системный метод __dict__ для Peter

print('='*18, 'Отображение словаря атрибутов для Peter:', '='*18)
print(f'\n{Peter.__dict__}\n')
# Получим результат:
# {'firstname': 'Peter', 'lastname': 'Pettigrew', 'age': 38, 'position': 'tail'}

# Сравниваем размеры классов с использованием слотов и без:
print('=' * 11, 'Результат с использованием функции asizeof: ', '=' * 11)
print(f'\nРазмер стандартного экземпляра класса Human: {asizeof.asizeof(Peter)} байт')
print(f'Размер экземпляра класса со слотами HumanSlots: {asizeof.asizeof(Peter_slots)} байт\n')
print('=' * 10, 'Результат с использованием функции getsizeof:', '=' * 10)
print(f'\nРазмер стандартного экземпляра класса Human: {getsizeof(Peter)} байта')
print(f'Размер экземпляра класса со слотами HumanSlots: {getsizeof(Peter_slots)} байт')

# Определили размер функцией asizeof и получили результат:
# Размер стандартного экземпляра класса Human: 376 байт
# Размер экземпляра класса со слотами HumanSlots: 160 байт
# Определим размер функцией getsizeof и получим совершенно
# противоположный результат:
# Для стандартного экземпляра класса Human: 32 байта
# Для экземпляра класса со слотами: 40 байт
#
# Вывод:
# Функция sys.getsizeof возвращает размер переданного ей обьекта,
# этот размер не включает в себя сложные структуры классов и т.д.
# Функция pympler.asizeof - рекурсивно ищет всё вложенние поля и
# элементы, и отображает общий размер обьекта.
# P.S. хочу заметить то, что размер, получаемый pympler.asizeof,
# тоже может являться не точным, функция пытается собрать полный
# размер обьекта, но со сложными структурами данных это не всегда
# получается.
# В данном случае можно опираться на показания pympler.asizeof,
# соответственно, если нет необходимости создавать новые атрибуты
# класса, предпочтительнее использование слотов для экономии памяти.
