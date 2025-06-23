# 1. Напишите функцию make_sentence, которая принимает один именованный
# аргумент words, который должен быть списком строк, и возвращает строку,
# составленную из элементов списка, разделенных пробелами и
# заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию
# используется список ["This", "is", "a", "sentence"].
from functools import reduce


# def make_sentence(words=None) -> str:
#     if words is None:
#         words = ["This", "is", "a", "sentence"]
#     return " ".join(words) + "."
#
#
# print(make_sentence(["California", "dreaming", "on", "such", "a", "winter's", "day"]))
#
#
# print(make_sentence())


# 2. Напишите функцию sum_of_squares, которая принимает произвольное
# количество позиционных аргументов, которые должны быть числами, и
# возвращает сумму их квадратов. Если функции не передано ни одного
# аргумента, она должна вернуть 0.

# def sum_of_squares(*args: int):
#     if len(args) == 0:
#         return 0
#     else:
#         for arg in args:
#             if not isinstance(arg, (int, float)):
#                 return "В функцию переданы не числа"
#             else:
#                 return sum(map(lambda x: x**2, args))
#
#
# print(sum_of_squares())
# print(sum_of_squares(0))
# print(sum_of_squares("qqewrf"))
# print(sum_of_squares(1, 2, 3, 4, 5))


# 3) Напишите функцию greet, которая принимает два именованных аргумента:
# name и language. Аргумент name должен быть строкой, а аргумент language
# должен быть одним из трех возможных значений: "en", "ru" или "fr".
# Функция должна возвращать приветствие на выбранном языке.
# # Если аргумент language не указан, то по умолчанию используется "en".
#
# def greet(name: str, language: str = "en"):
#     if not (isinstance(name, str) and isinstance(language, str)):
#         return "Переданное имя или язык не являются строкой"
#     if language == "ru":
#         return f"Привет, {name}!"
#     elif language == "en":
#         return f"Hello, {name}!"
#     elif language == "fr":
#         return f"Bonjour, {name}!"
#
#
# print(greet(language="ru", name="Polly"))
# print(greet(language="en", name="Alex"))
# print(greet(name="Kate", language="fr"))
# print(greet(name="Kate", language=2))
# print(greet(name="Sheldon"))


# 4) Напишите функцию print_info, которая принимает произвольное
# количество именованных аргументов (**kwargs) и выводит их в формате
# "key: value" по одной паре на строку. Напоминаю, что kwargs в функции
# будет словарем. Если функции не передано ни одного аргумента, она должна
# вывести "No info given.".

# def print_info(**kwargs):
#     if len(kwargs) == 0:
#         print("No info given.")
#     else:
#         for key, value in kwargs.items():
#             print(f"{key}: {value}")
#
#
# print_info()
# print_info(first="polly", second="sofi", third="mila")


# 5) Напишите функцию print_table, которая принимает произвольное
# количество именованных аргументов в виде пар ключ-значение и выводит их
# в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не
# передано ни одного аргумента, она должна вывести "No data given.".

# def print_info(**kwargs):
#     if len(kwargs) == 0:
#         print("No data given.")
#     else:
#         max_len_key = len(max(kwargs.keys(), key=lambda x: len(x)))
#         max_len_value = len(max(kwargs.values(), key=lambda x: len(str(x))))
#
#         print(f"| {"Key":^{max_len_key}} | {"Value":^{max_len_value}} |")
#         print(f"| {"_" * max_len_key} | {"_"*max_len_value} |")
#
#         for key, value in kwargs.items():
#             print(f"| {key:^{max_len_key}} | {value:^{max_len_value}} |")
#
#
# print_info()
# print_info(name="Donni", age=34, city="California")


# 6) Напишите функцию calculate, которая принимает произвольное количество
# позиционных аргументов, которые должны быть числами, и один
# именованный аргумент operation, который должен быть одним из четырех
# возможных значений: "+", "-", "*" или "/".
# Функция должна возвращать результат выполнения указанной операции над
# всеми числами в порядке их передачи.
# Если функции не передано ни одного позиционного аргумента, она должна
# вернуть 0.
# Если аргумент operation не указан, то по умолчанию используется "+".


# def make_operation(*args: int, operation: str = "+"):
#     if len(args) == 0:
#         return 0
#     if operation == "+":
#         return sum(args)
#     if operation == "-":
#         return args[0] - sum(args[1:])
#     if operation == "*":
#         return reduce(lambda x, y: x * y, args)
#     if operation == "/":
#         return reduce(lambda x, y: x / y, args)
#
#
# print(make_operation(20, 5, 1, operation="+"))
# print(make_operation(20, 5, 1))
# print(make_operation(20, 5, 1, operation="-"))
# print(make_operation(20, 5, 3, operation="*"))
# print(make_operation(20, 5, 2, 4, operation="/"))


# 7)  Напишите функцию print_triangle, которая принимает один именованный
# аргумент height, который должен быть положительным целым числом, и
# выводит равнобедренный треугольник из символов "*" с заданной высотой.
# Если аргумент height не указан, то по умолчанию используется число 5.

# def print_triangle(height:int=5):
#     if not (isinstance(height, int) and height >= 0):
#         print("Задана некорректная высота треугольника")
#     for i in range(height):
#         if i == 0:
#             print(f"{"*":^{height*2}}")
#         else:
#             print(f"{("*"*(1+i*2)):^{height*2}}")
#
# print_triangle()
# print_triangle(10)
# print_triangle(-234)

# 8) Напишите функцию create_post, которая создает пост для блога,
# основываясь на переданных параметрах. Обязательными параметрами
# являются: заголовок, содержимое и автор. Необязательным параметром
# является категория. Если она не была передана, то по умолчанию будет
# текущая значение “general”. Функция должна возвращать словарь поста.

# def create_post(header, content, author, category="general"):
#     post_dict = {
#         "header": header,
#         "content": content,
#         "author": author,
#         "category": category
#     }
#     return post_dict
#
# print(create_post("I'm in LA", "I'm so happy to be here!!!", "Ann Border", "travelling"))
# print(create_post("I'm in Kaluga", "I'm so happy to be here!!!", "Kirill Druh"))


# 9) Напишите функцию create_product, которая создает товар для интернет-магазина,
# основываясь на переданных параметрах. Обязательными
# параметрами являются: имя, цена и категория. Необязательным параметром
# является рейтинг. Если он не был передан параметр, то по умолчанию будет
# 0. Функция должна возвращать словарь товара.

# def create_product(name, cost, category, rating=0):
#     product = {
#         'name': name,
#         'cost': cost,
#         'category': category,
#         'rating': rating
#     }
#     return product
#
#
# print(create_product("tomato", "7$", "food"))
# print(create_product("textbook", "4$", "office", 4.8))


# 10) Напишите функцию create_student, которая создает словарь студента
# для учебного заведения, основываясь на переданных параметрах.
# Обязательными параметрами являются: имя, фамилия, отчество и группа.
# Также дополнительными параметрами могут быть: дата поступления в виде
# строки «19.10.2023», средний бал, семестр обучения, номер телефона, адрес.
# Функция должна возвращать словарь студента только с переданными
# данными, если некоторые данные не были переданы, то их не должно быть
# в словаре.

def create_student(first_name, last_name, middle_name, group_number,
                   enter_date=None, avg_rate=None, semester=None, phone_number=None, address=None):
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'middle_name': middle_name,
        'group_number': group_number,
    }

    if enter_date is not None:
        student['enter_date'] = enter_date
    if avg_rate is not None:
        student['avg_rate'] = avg_rate
    if semester is not None:
        student['semester'] = semester
    if phone_number is not None:
        student['phone_number'] = phone_number
    if address is not None:
        student['adress'] = address

    return student

print(create_student("Иван", "Иванов", "Иванович", "БИВТ-23-01"))
print(create_student("Анна", "Сидорова", "Петровна", "ИКБО-21-03", avg_rate=4.8))
print(create_student("Елена", "Миронова", "Викторовна", "ПМИ-22-05",
               enter_date="2022-09-01", avg_rate=4.3, semester=2,
               phone_number="+79005556677", address="г. Москва, ул. Примерная, д. 5"))
