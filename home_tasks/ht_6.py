# #функции
#
#
# # функция без аргументов (параметров)
# def say_hello():
#     print("Hello")
#
#
# say_hello()
#
#
#
# # функция с параметрами
# def multiply(num1, num2):
#     return num1 * num2
#
#
# num3 = multiply(8, 5)
# print(num3)
#
#
# # изменённый порядок аргументов
# def say_numbers(num1, num2):
#     print(f"num1 = {num1}")
#     print(f"num2 = {num2}")
#
#
# say_numbers(24, 534)
# say_numbers(num2=24, num1=534)
#
#
# # функция с параметрами по умолчанию
# def summation(num1, num2=8):
#     return num1 + num2
#
# # вызов функции без передачи аргумента по умолчанию
# num3 = summation(5)
# print(num3)
#
# # вызов функции с передачей аргумента по умолчанию с отличным от дефолтного значением
# num4 = summation(5, 24)
# print(num4)
#
# # параметры по умолчанию указываются ПОСЛЕ обычных параметров, иначе ошибка
# # тут вылетит ERROR
#
# def minus(num1=34, num2):
#     return num1 - num2
#
#
# num5 = minus(5, 24)
# print(num5)
#
#
# #функция с неизвестным (любым) количеством аргументов
# def summing(*args):
#     sum = 0
#     for num in args:
#         print(f"num = {num}")
#         sum += num
#     return sum
#
#
# print(summing(2, 5, 5, 34))

# ---------------------- Home Tasks ----------------------

# # Задание 1.
# # Напишите функцию, которая принимает на вход строку (предложение), а возвращает самое длинное слово из строки.
# def longest_word(text):
#     splitted_text = text.split(' ')
#     largest_world = ''
#     for word in splitted_text:
#         if len(word) > len(largest_world):
#             largest_world = word
#
#     return largest_world
#
# print(longest_word("Официальное название: смерть от чрезмерного усердия."))


# # Задание 2.
# # Напишите функцию, которая принимает на вход строку и заменяет в ней все множественные пробелы на одинарные.
# #       Например: 'Hello,    world' -> 'Hello, world'
#
# def replace_multiple_spaces(text):
#     split_text = text.split()
#     new_text = ''
#     for word in split_text:
#         if word is not split_text[-1]:
#             new_text += word + ' '
#         else:
#             new_text += word
#     return new_text
#
# print(replace_multiple_spaces("В этом    мире нет      ничего         вечного"))


# # Задание 3.
# # Напишите функцию, которая принимает на вход строку и возвращает словарь,
# # где ключи - это символы, а значения - количество этих символов в строке.
# #       Например: 'Hello, world!' -> {'H': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
# #       Подсказка: используйте метод строки `count("a")`, который возвращает количество вхождений символа в строку.
#
# def count_letters(text):
#     my_dict = {}
#     for char in text:
#         my_dict[char] = text.count(char)
#
#     return my_dict
#
#
# print(count_letters("Hello, world!"))
#
# # но тут мы перебираем дважды
# # setdefault возвращает значение по ключу (первый аргумент), если ключа нет,
# # то создаётся новый ключ (первый аргумент) и ему присваивается значение (второй аргумент)
# # таким образом, сокращаем количество проходок по списку и т.д.
# # второй вариант
#
#
# def count_letters_2(text):
#     my_dict = {}
#     for char in text:
#         my_dict[char] = my_dict.setdefault(char, 0) + 1
#
#     return my_dict
#
#
# print(count_letters_2("Hello, world!"))



# # Задание 4.
# # Напишите функцию, которая принимает на вход строку и возвращает True,
# # если строка является палиндромом, и False - в противном случае.
# #       Палиндром - это строка, которая читается одинаково в обоих направлениях.
# #       Например: 'мадам', 'А роза упала на лапу Азора'
#
# #
# def is_palindrome(text):
#     for char in text:
#         if not char.isalpha():
#             text = text.replace(char, '')
#
#     for i in range(int(len(text) / 2)):
#         if text[i].lower() != text[len(text) - i - 1].lower():
#             return False
#
#     return True
#
# print(is_palindrome("шалаш"))
# print(is_palindrome("Шалаш"))
# print(is_palindrome("А роза упала на лапу Азора"))


# Задание 5.
# Напишите функцию, которая принимает на вход строку и возвращает новую строку,
#       в которой все символы, которые не являются буквами, удалены (пробел разрешен).
#       Например: 'Hello, world!' -> 'Hello world'
#       Подсказка: используйте цикл и метод строки `isalpha()` для проверки, является ли символ буквой.
def remove_non_letters(text):
    for char in text:
        if not (char.isalpha() or char == " "):
            text = text.replace(char, '')
    return text

print(remove_non_letters("Hello!!!, ~I am~ here))) ---again!!!!"))


# # Задание 6.
# # Напишите функцию, которая принимает на вход строку и возвращает новую строку,
# # в которой все гласные буквы заменены на символ '*'.
# def replace_vowels(text):
#     vowels = "aeiouаеёиоуыэюя"
#
#     for char in text:
#         if char.lower() in vowels:
#             text = text.replace(char, "*")
#     return text
#
#
# print(replace_vowels("Функция, которая принимает на вход строку и возвращает новую строку"))

# # Задание 7.
# # Напишите функцию, которая принимает на вход число и возвращает сумму его цифр.
# def sum_digits(number):
#     sum = 0
#     while number > 0:
#         sum += number % 10
#         number = int(number / 10)
#     return sum
#
# print(sum_digits(12329))


# # Задание 8.
# # Напишите функцию, которая принимает на вход число и возвращает True,
# # если число является степенью двойки, и False - в противном случае.
# #       Например: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536 и т.д.
# #       Подсказка: используйте цикл и оператор деления без остатка.
# def is_power_of_two(number):
#     if(type(number) != int or number < 0):
#         return False
#     while number > 1:
#         number /= 2
#     return bool(int(number))
#
# print(is_power_of_two(32))
# print(is_power_of_two(6))
# print(is_power_of_two(5.1))
# print(is_power_of_two(-353))


# # Задание 9.
# # Напишите функцию, которая принимает на вход три целых числа и возвращает True,
# # если они могут быть длинами сторон треугольника.
# #       Подсказка: сумма двух сторон треугольника должна быть больше третьей стороны.
# def is_triangle(a, b, c):
#     if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
#         return "Введены не целые числа"
#     elif(a + b < c or b + c < a or c + a < b or a <= 0 or b <= 0 or c <= 0):
#         return False
#     else:
#         return True
#
#
# print(is_triangle(5.4, 6, 7))
# print(is_triangle(5, -66, 7))
# print(is_triangle(5, 6, 7))
# print(is_triangle(19, 6, 7))


# # Задание 10.
# # Напишите функцию, которая принимает на вход строку и возвращает новую строку, в которой все символы,
# # которые встречаются более одного раза, заменены на символ '_'.
# def replace_duplicates(text):
#     for char in text:
#         if text.count(char) > 1:
#             text = text.replace(char, '_')
#     return text
#
#
# print(replace_duplicates("ahahahah, dobroe utro"))
