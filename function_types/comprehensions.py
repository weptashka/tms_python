# #------------ LIST ----------------
#
# some_str = 'alk234-w75e34lfvn'
# digits = [int(i) for i in some_str if '0' <= i <= '9']
# print(digits)
#
#
# # заполнить список числами, кратными 30 и 31
# list_1 = [i for i in range(0, 340) if i % 30 == 0 or i % 31 == 0]
# print(list_1)
#
#
# # генераторы списков можно делать вложенными друг в друга.
# # Это позволит создать многомерные массивы (например, матрицы)
# N = 4
# matrix = [[0 for i in range (N)] for j in range(N)]
# for row in matrix:
#     print(row)
#
#
# # Переменные в цикле - глобальные, в функции - локальные, в comprehensions - локальные.
#
# # цикл - i -  глобальная
# for i in range(1, 5):
#     print("Итерация: ", i)
# print(i)
#
#
# # цикл в функции - j - локальная
# def funk_1():
#     for i in range(1, 5):
#         print("Итерация: ", j)
#
#
# funk_1()
# print(j)
#
#
# # переменная t в comprehensions - локальная
# arr = [t for t in range(8, 23)]
# print(arr)
# print("t = "t)



#------------ DICT ----------------

# примеры
dict_1 = {x: x**2 for x in range(5)}
print(dict_1)

dict_2 = {x: x**2 for x in (7, 9, 11, 12)}
print(dict_2)


# + условие
dict_3 = {x: x**2 for x in range(10) if x % 3 == 0}
print(dict_3)



#------------ SET ----------------

set_1 = {x for x in 'jasbdvij' if x not in 'jabd'}
print(set_1)