# Функция sorted() возвращает новый отсортированный список
# итерируемого объекта (списка, словаря, кортежа).
# По умолчанию она сортирует его по возрастанию.

# Сортировка строк осуществляется по ASCII-значениям.

# Возвращаемое значение — List (список).
# Синтаксис: sorted(iterable,key=None,reverse=False).
# iterable: строка, список, кортеж, множество, словарь
# key (необязательный параметр): если указать ключ, то сортировка будет выполнена по функции этого ключа.
# reverse (необязательный параметр): по умолчанию сортировка выполняется по возрастанию.
# Если указать reverse=True, то можно отсортировать по убыванию.


# Сортировка строки
# H впереди, так как по ASCII код меньше
s2 = "Hello"
print(sorted(s2))  # Вывод:['H', 'e', 'l', 'l', 'o']
print(sorted(s2, reverse=True))   # Вывод:['o', 'l', 'l', 'e', 'H']

# Сортировка списка
l1 = [1, 4, 5, 2, 456, 12]
print(sorted(l1))   # Вывод:[1, 2, 4, 5, 12, 456]
print(sorted(l1, reverse=True))   # Вывод:[456, 12, 5, 4, 2, 1]

# Сортировка кортежа
t1 = (15, 3, 5, 7, 9, 11, 42)
print(sorted(t1))   # Вывод:[3, 5, 7, 9, 11, 15, 42]
print(sorted(t1, reverse=True))   # Вывод:[42, 15, 11, 9, 7, 5, 3]

# Сортировка списка кортежей

# Когда ты вызываешь sorted() на списке кортежей,
# Python сортирует их лексикографически по умолчанию —
# то есть по первому элементу, затем по второму, если первые равны, и так далее.
t2 = [(1, 2), (11, 12), (0, 2), (3, 2)]
print(sorted(t2))   # Вывод:[(0, 2), (1, 2), (3, 2), (11, 12)]
print(sorted(t2, reverse=True))   # Вывод:[(11, 12), (3, 2), (1, 2), (0, 2)]



# Сортировка множества
s1 = {1, 4, 3, 6, 2, 8, 11, 32}
print(sorted(s1))   # Вывод:[1, 2, 3, 4, 6, 8, 11, 32]
print(sorted(s1, reverse=True))   # Вывод:[32, 11, 8, 6, 4, 3, 2, 1]

# Сортировка словаря
d1 = {2: 'red', 1: 'green', 3: 'blue'}
# Вернется список отсортированных ключей
print(sorted(d1))   # Вывод:[1, 2, 3]

# Вернется список отсортированных значений
print(sorted(d1.values()))   # Вывод:['blue', 'green', 'red']

# Вернется список кортежей (ключ, значение), отсортированный по ключам.
print(sorted(d1.items()))   # Вывод:[(1, 'green'), (2, 'red'), (3, 'blue')]

# Сортировка словаря в обратном порядке
print(sorted(d1, reverse=True))   # Вывод:[3, 2, 1]
print(sorted(d1.values(), reverse=True))   # Вывод:['red', 'green', 'blue']
print(sorted(d1.items(), reverse=True))   # Вывод:[(3, 'blue'), (2, 'red'), (1, 'green')]