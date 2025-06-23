# 1) Напишите код, который принимает список чисел и возвращает новый список,
# содержащий только четные числа из исходного списка. Используйте функцию
# filter и лямбда-выражение.

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def filter_even_numbers(numbers: list) -> list:
#     return list(filter(lambda x: x % 2 == 0, numbers))
#
#
# print(filter_even_numbers(numbers_list))


# 2) Напишите код, который принимает список кортежей вида (имя, возраст) и
# возвращает новый список, отсортированный по возрастанию возраста.
# Используйте функцию sorted и ключ сортировки.

# users = [("polly", 22), ("maxim", 19), ("sonya", 19), ("dasha", 27)]
#
#
# def sort_by_age(persons) -> list:
#     return sorted(persons, key=lambda person: person[1])
#
#
# print(sort_by_age(users))


# 3) Напишите код, который принимает список строк и возвращает новый список,
# содержащий только те строки, которые начинаются с гласной буквы. (Да да,
# снова эти гласные) Используйте функцию filter и множество.

# my_strings = ["загадочный", "танец", "апельсин", "оранжевое", "apple", "pillow"]
#
#
# def vowel_start_strings(strings) -> list:
#     return list(filter(lambda x: x[0].lower() in 'уеоаыяюaeiou', strings))
#
#
# print(vowel_start_strings(my_strings))


# 4) Напишите код, который принимает список чисел и возвращает новый список,
# содержащий квадраты этих чисел. Используйте функцию map и lambda.

# numbers = [1, 2, 3, 4, 5, 11, 23, 45]
#
#
# def squred_numbers(numbers_list) -> list:
#     return list(map(lambda number: number ** 2, numbers_list))
#
#
# print(squred_numbers(numbers))


# 5) Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по убыванию длины слов. Используйте функцию sorted и
# обратный порядок сортировки.

# song_lyrics = ["Maybe", "we", "could", "devide", "it", "in", "two"]
#
#
# def sort_by_len(words) -> list:
#     return list(sorted(words, key=lambda word: len(word), reverse=True))
#
#
# print(sort_by_len(song_lyrics))


# 6) Напишите код, который принимает строку и возвращает список, содержащий
# только те буквы, которые встречаются в слове “python”. Используйте функцию
# filter и оператор in.

# song_lyrics_2 = "Crystal bits of snowflake all around my head"
#
#
# def letters_in_python(text) -> list:
#     return list(filter(lambda char: char in "python", text))
#
#
# print(letters_in_python(song_lyrics_2))


# 7) Напишите код, который принимает список чисел и возвращает новый список,
# содержащий эти же числа, умноженные на 10. Используйте функцию.

# my_numbers = [1, 2, 34, -233, 0, 8]
#
#
# def multiplication_by_10(numbers: list) -> list:
#     return list(map(lambda x: x * 10, numbers))
#
#
# print(multiplication_by_10(my_numbers))


# 8) Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по алфавиту. Используйте функцию sorted.

# song_lyrics = ["Maybe", "we", "could", "Devide", "It", "in", "two"]
#
#
# def sort_by_alphabet(words: list) -> list:
#     return list(sorted(words, key=lambda word: word.lower()))
#
#
# print(sort_by_alphabet(song_lyrics))

# 9) Напишите функцию, которая принимает список строк и возвращает новый
# список, содержащий только те строки, которые являются палиндромами.
# Палиндром — это слово, которое читается одинаково слева направо и справа
# налево. Используйте функцию filter и сравнение строк.
# some_words = ["hello", "world", "goodbye", "шалаш", "pop", "А роза упала на лапу Азора"]
#
#
# def is_palindrome(word):
#     word = word.replace(" ", "").lower()
#     return word == word[::-1]
#
# def get_only_palindromes(words: list) -> list:
#     return list(filter(is_palindrome, words))
#
#
# print(get_only_palindromes(some_words))


# 10) Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества гласных букв в словах.
# Используйте функцию sorted и ключ сортировки.

# song_lyrics = ["Maybe", "my", "animals", "live", "zoo", "abracadabra"]
#
#
# def sort_by_number_of_vowels(words: list) -> list:
#     return sorted(words, key=lambda word: sum(1 for char in word.lower() if char in "aeiouyйуеэоаыяию"))
#
#
# print(sort_by_number_of_vowels(song_lyrics))

# 11) Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки в верхнем регистре. Используйте функцию map и
# встроенный метод строк upper.

# song_lyrics = ["Maybe", "we", "could", "Devide", "It", "in", "two"]
#
# def make_strings_uppercase(words: list) -> list:
#     return list(map(lambda word: word.upper(), words))
#
#
# print(make_strings_uppercase(song_lyrics))


# 12) Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки с добавленным префиксом “Hello”. Используйте
# функцию map и конкатенацию строк.

# song_lyrics = ["Maybe we", "could", "Devide", "It", "in", "two"]
#
#
# def add_hello(words: list) -> list:
#     return list(map(lambda word: "Hello" + word, words))
#
#
# print(add_hello(song_lyrics))


# 13) Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества букв “a” в словах. Используйте
# функцию sorted и ключ сортировки.

# song_lyrics = ["Maybe", "can", "abracadabra", "impressive", "banana", "apple"]
#
#
# def sort_by_number_of_a(words: list) -> list:
#     return sorted(words, key=lambda word: word.lower().count('a'))
#
#
# print(sort_by_number_of_a(song_lyrics))


# 14) Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества уникальных букв в словах.
# Используйте функцию sorted и ключ сортировки.

# song_lyrics = ["Maybe", "can", "abracadabra", "impressive", "banana", "apple"]
#
#
# def sort_by_uniq_letters_number(words: list) -> list:
#     return sorted(words, key=lambda word: len(set(word.lower())))
#
#
# print(sort_by_uniq_letters_number(song_lyrics))

# 15) Напишите декоратор retry_five, который повторяет вызов декорируемой
# функции 5 раз.

def retry_five(inner_function):
    def output_function():
        inner_function()
        inner_function()
        inner_function()
        inner_function()
        inner_function()
    return output_function

@retry_five
def simple_function():
    print("Я простая функция")


simple_function()
