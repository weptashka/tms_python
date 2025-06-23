# Сумма трёх чисел
# Напишите программу, которая считывает три целых числа и выводит на
# экран их сумму. Каждое число записано в отдельной строке.
# Ввод:
# 1
# 2
# 3
# Вывод:
# 6


# print("Ввод:")
#
# x_1 = int(input())
# x_2 = int(input())
# x_3 = int(input())
#
# print("Вывод:\n", x_1 + x_2 + x_3)



# Следующее и предыдущее
# Напишите программу, которая считывает целое число, после чего на
# экран выводится следующее и предыдущее целое число с
# пояснительным текстом.
# Ввод:
# 10
# Вывод:
# Следующее за числом 10 число: 11
# Для числа 10 предыдущее число: 9

# print("Ввод:")
# x = int(input())
#
# print("Вывод: ")
# print(f"Следующее за числом {x} число: ", x + 1)
# print(f"Для числа {x} предыдущее число: ", x - 1)


# Расстояние в метрах
# Напишите программу, которая находит полное число метров по
# заданному числу сантиметров.
# Ввод:
# 3561
# Вывод:
# 35 метров

# print("Ввод:")
# x = int(input())
#
# print("Вывод: ")
# print(int(x / 100), "метров")


# Пересчет временного интервала
# Напишите программу для пересчёта величины временного интервала,
# заданного в минутах, в величину, выраженную в часах и минутах.
# Ввод:
# 90
# Вывод:
# 90 мин — это 1 час 30 минут

# print("Ввод:")
# x = int(input())
#
# print("Вывод: ")
# print(f"{x} минут - это {int(x / 60)} час(-ов)(-а) и {x % 60} минут(-ы)")


# Трехзначное число
# Напишите программу, в которой рассчитывается сумма и произведение
# цифр положительного трёхзначного числа.
# Ввод:
# 132
# Вывод:
# Сумма цифр = 6
# Произведение цифр = 6

#если именно трёхзначное
# print("Ввод:")
# x = int(input())
#
# print("Вывод: ")
# print(f"Сумма цифр = {int(x / 100) + int(x / 10) - int(x / 100) * 10 + x - int(x / 10) * 10}")
# print(f"Произведение цифр = {int(x / 100) * (int(x / 10) - int(x / 100) * 10) * (x - int(x / 10) * 10)}")


#вариант через строки
# print("Ввод:")
# x = int(input())
#
# print("Вывод: ")
# print(f"Сумма цифр = {int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2])}")
# print(f"Произведение цифр = {int(str(x)[0]) * int(str(x)[1]) * int(str(x)[2])}")

# Четное или нечетное?
# Напишите программу, которая определяет, является число четным или
# нечетным.
# Ввод:
# 132
# Вывод:
# Четное

# print("Ввод:")
# x = int(input())
#
# print("Вывод: ")
# print("Чётное" if (x % 2) == 0 else "Нечётное")


# Квадрат
# Написать программу, принимающую 1 аргумент — сторону квадрата, и
# возвращающую 3 значения: периметр квадрата, площадь квадрата и
# диагональ квадрата.
# Ввод:
# 3
# Вывод:
# Периметр равен: 12
# Площадь равна: 9
# Диагональ квадрата равна: 4.242640687119286

# import math
#
# x = float(input("Ввод: \n"))
#
# print("Вывод: ")
# print(f"Периметр равен: {x * 4}")
# print(f"Площадь равна: {x ** 2}")
# print(f"Диагональ квадрата равна: {math.sqrt(x ** 2 * 2)}")


# СПИСКИ
# 1. Создать произвольный список
# 2. Добавить новый элемент типа str в конец списка
# 3. Добавить новый элемент типа int на место с индексом
# 4. Добавить новый элемент типа list в конец списка
# 5. Добавить новый элемент типа tuple на место с
# индексом
# 6. Получить элемент по индексу
# 7. Удалить элемент

# my_list = [1, 2, 3, 4, 5]
# print("1.", my_list)
# print(type(my_list), "\n")
#
# my_list.append("this_is_string")
# print("2.", my_list)
# print(f"{my_list[-1]} - {type(my_list[-1])}\n")
#
# my_list.insert(3, 22)
# print("3.", my_list)
# print(f"{my_list[3]} - {type(my_list[3])}\n")
#
# my_list.append(["yellow", "submarine"])
# print("4.", my_list)
# print(f"{my_list[-1]} - {type(my_list[-1])}\n")
#
# my_list.insert(2, ("ahaha", "hahaha"))
# print("5.", my_list)
# print(f"{my_list[2]} - {type(my_list[2])}\n")
#
# print("6.", my_list[0], "\n")
#
# my_list.remove(22)
# print("7.", my_list)


# СЛОВАРИ
# 1. Создать произвольный словарь
# 2. Добавить новый элемент с ключом типа str и значением
# типа int
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и
# значением типа список(list)
# 4. Получить элемент по ключу
# 5. Удалить элемент по ключу

# #  1
# people = {
#     "Sasha": 25,
#     "Masha": 30,
#     "Pasha": 22
# }
#
# for name, age in people.items():
#     print(f"{name}: {age} лет")
# print()
#
# #  2
# people["Lesha"] = 16
#
# for name, age in people.items():
#     print(f"{name}: {age} лет")
# print()
#
# #  3
# people[("Zenya", "Marina")] = [50, 47]
#
# for name, age in people.items():
#     print(f"{name}: {age} лет")
# print()
#
# #  4
# print(people.get("Masha"))
# print()
#
# for name, age in people.items():
#     print(f"{name}: {age} лет")
# print()
#
# #  5
# people.pop(("Zenya", "Marina"))
#
# for name, age in people.items():
#     print(f"{name}: {age} лет")




# words = ["1Й РАЗ", "2Й РАЗ", 1234.4, "4Й РАЗ"]
#
# new_words = []
#
# for element in words:
#     if not isinstance(element, str):
#         element = str(element)
#     new_words.append(element.lower())
#
#
# for new_word in new_words:
#     print(new_word)
#     print(type(new_word))


# -----------------------
# ------ Словари --------
# -----------------------

# создание словаря
# users_hobby = {
#     'Polly': 'drawing',
#     'Sofi': 'painting',
#     'Mila': 'tik tok'
# }

# print(type(users_hobby))
#
# print(users_hobby)

# # если использовать не двоеточие, а запятую, получится множество,
# # и в нём будут только "ключи", будто мы не указали "значений"
# users_hobby_2 = {
#     'Polly', 'drawing',
#     'Sofi', 'drawing',
#     'Mila', 'tik tok'
# }
#
# print(type(users_hobby_2))
#
# for i in users_hobby_2:
#     print(i)
#
# print(users_hobby_2)

# доступ к значениям по ключу
# print(users_hobby['Polly'])
# print(users_hobby['Poll'])

# print(users_hobby)
# users_hobby['Nataly'] = 'dancing'
# print(users_hobby)
# del users_hobby['Sofi']
# print(users_hobby)
