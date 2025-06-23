# # Задание 1
# # Через цикл вывести в консоль все элементы списка.
# # Используя цикл, вывести в консоль все элементы списка в обратном порядке.
# # Используя цикл, вывести в консоль все элементы списка, а их буквы в обратном порядке.
# list1 = ['apple', 'banana', 'cherry']
#
# print("элементы списка:")
# for word in list1:
#     print(word)
#
# print("элементы списка в обратном порядке:")
# i = len(list1) - 1
# while i >= 0:
#     print(list1[i])
#     i = i - 1
#
# print("элементы списка, а их буквы в обратном порядке:")
# for word in list1:
#     print(word[::-1])


# # Задание 2
# # Используя цикл, вывести в консоль все ключи словаря.
# # Используя цикл, вывести в консоль все ключи и значения словаря.
# dict1 = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
#
# print("Ключи словаря: ")
# for key in dict1:
#     print(key)
#
# print("Ключи и значения словаря: ")
# for key, value in dict1.items():
#     print(f"{key} : {value}")


# # Задание 3
# # На вход пользователь вводит целое число (использовать функцию input).
# # Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно.
# # Используя цикл, вывести в консоль все числа от введенного числа до 1 включительно.
# # Используя цикл, вывести в консоль все числа от 1 до введенного числа включительно, которые делятся на 3 без остатка.
#
# num = int(input("Введите целое число:\n"))
#
# print("По порядку: ")
# for i in range(1, num + 1):
#     print(i)
#
# print("\n В обратном порядке: ")
# for i in range(num, 0, -1):
#     print(i)
#
# print("\n Делятся на 3 без остатка: ")
# for i in range(1, num + 1):
#     if i % 3 == 0:
#         print(i)

# # Задание 4
# # На вход пользователь вводит предложение (использовать функцию input).
# # Посчитайте количество слов в предложении и выведите результат в консоль.
# # Используя цикл, выведите в консоль все слова предложения в обратном порядке.
# # Используя цикл, создайте словарь, где ключами являются длина слов,
# #           а значениями - список слов в предложении с такой длиной.
#
# text = str(input("Введите предложение: \n"))
#
# print("Количество слов в предложении: ")
# for letter in text:
#     if not(letter.isalpha() or letter == " "):
#         text = text.replace(letter, "")
# print(len(text.split()))
#
#
# print("\nСлова в обратном порядке: ")
# new_text = text.split()
# new_text_2 = ''
# for i in range(len(new_text) - 1, -1, -1):
#     new_text_2 += new_text[i] + " "
# print(new_text_2)
#
#
# new_dict = {}
# for i in range(0, len(new_text)):
#     if len(new_text[i]) in new_dict:
#         new_dict[len(new_text[i])].append(new_text[i])
#     else:
#         new_dict[len(new_text[i])] = [new_text[i]]
#
# print("\nСловарь, где ключами является длина слова, а значение - список слов с такой длиной: ")
# print(new_dict)



# # Задание 5
# # На вход пользователь должен ввести username, email, имя и фамилию по очереди (использовать функцию input).
# # Для каждого параметра: если введенные данные не соответствуют требованиям
# # (например, username должен быть длиной от 3 до 20 символов),
# # выведите сообщение об ошибке и попросите ввести данные заново.
# # Создайте словарь с данными пользователя и выведите его в консоль.
#
# user_info = {}
#
# user_username = str(input("Введите username: "))
# while len(user_username) > 20 or len(user_username) < 3:
#     print("Не верная длина username. Введите от 3 до 20 символов.")
#     user_username = str(input("Введите username: "))
#
# user_info["username"] = user_username
#
#
# user_email = str(input("Введите email: "))
# while (not "@gmail.com" in user_email and not "@yandex.com" in user_email):
#     print("Не верный email. Введите почту Google/Yandex.")
#     user_email = str(input("Введите username: "))
#
# user_info["email"] = user_email
#
#
# user_first_name = str(input("Введите имя: "))
# while (
#         user_first_name[0] != user_first_name[0].upper()
#         or
#         user_first_name[1:len(user_first_name)] != user_first_name[1:len(user_first_name)].lower()
#         or
#         not user_first_name.isalpha()
# ):
#     print("Не верный формат имени. Имя должно содержать только буквы, "
#           "только первая буква имени должна быть заглавной")
#     user_first_name = str(input("Введите имя: "))
#
# user_info["user_first_name"] = user_first_name
#
#
# user_last_name = str(input("Введите фамилию: "))
# while (
#         user_last_name[0] != user_last_name[0].upper()
#         or
#         user_last_name[1:len(user_last_name)] != user_last_name[1:len(user_last_name)].lower()
#         or
#         not user_last_name.isalpha()
# ):
#     print("Не верный формат фамилии. Фамилия должна содержать только буквы, "
#           "только первая буква фамилии должна быть заглавной")
#     user_last_name = str(input("Введите фамилию: "))
#
# user_info["user_last_name"] = user_last_name
#
# print(user_info)


# Задание 6*
# Напишите в коде случайное число от 1 до 100.
# Пользователь должен угадать это число.
# Используя цикл, попросите пользователя ввести число до тех пор, пока он не угадает.
# Если пользователь ввел не число, выведите сообщение "Вы ввели не число".
# Если пользователь ввел число, которое не попало в диапазон от 1 до 100, выведите сообщение "Число не входит в диапазон от 1 до 100".
# Если пользователь ввел число больше загаданного, выведите сообщение "Загаданное число меньше".
# Если пользователь ввел число меньше загаданного, выведите сообщение "Загаданное число больше".
# Если пользователь угадал число, выведите сообщение "Вы угадали!" и завершите программу.

# тут можно один раз user_num к int привести

num = 5
user_num = 0
is_guessed = False
print("Вам нужно отгадать число от 1 до 100")

while not is_guessed:
    user_num = input("Введите число: ")
    if not user_num.isdigit():
        print("Вы ввели не число")
    elif int(user_num) > 100 or int(user_num) < 1:
        print("Число не входит в диапазон от 1 до 100")
    elif int(user_num) > num:
        print("Загаданное число меньше")
    elif int(user_num) < num:
        print("Загаданное число больше")
    elif int(user_num) == num:
        print("Вы угадали!")
        is_guessed = True


# # Задание 7*
# # Имеется структура данных пользователя.
#
# # Используя цикл, выведите все активности по логам пользователя в консоль со временем и описанием.
# # Если пользователь активен, выведите сообщение "Пользователь активен", иначе выведите "Пользователь не активен".
# # Если у пользователя есть аватар, то выведите его в консоль, если нет, то выведите "Нет аватара".
#
# user1 = {
#     "userId": 2,
#     "username": "janedoe",
#     "email": "janedoe@example.com",
#     "profile": {
#         "firstName": "Jane",
#         "lastName": "Doe",
#         "birthDate": "1992-04-12",
#         "gender": "female",
#         "avatarUrl": "https://example.com/avatars/janedoe.jpg",
#         "bio": "Digital marketer and blogger."
#     },
#     "accountStatus": {
#         "isActive": True,
#         "lastLogin": "2025-01-10T09:15:00Z",
#         "createdAt": "2023-03-20T11:00:00Z"
#     },
#     "activityLogs": [
#         {
#             "timestamp": "2025-01-09T18:30:00Z",
#             "activity": "Commented on a post"
#         },
#         {
#             "timestamp": "2025-01-08T16:45:00Z",
#             "activity": "Liked a post"
#         }
#     ]
# }
#
#
# for activity_log in user1["activityLogs"]:
#     print(f"{activity_log["timestamp"]} {activity_log["activity"]}")
#
# if user1["accountStatus"]["isActive"]:
#     print("Пользователь активен")
# else:
#     print("Пользователь не активен")
#
# if user1["profile"]["avatarUrl"]:
#     print(user1["profile"]["avatarUrl"])
# else:
#     print("Нет аватара")


# # Задание 8*
#
# # Имеется структура данных продукта.
#
# # Сейчас кол-во товара на складе равно 0. Посчитайте кол-во исходя из вариантов товара на складе.
# # Выведите через цикл все варианты товара на складе в виде строки в формате: "Название - цена (кол-во на складе)".
# # Используя цикл, найдите вариант товара с максимальной ценой и выведите его название и цену в консоль.
# # Выведите через цикл все отзывы о товаре в виде строки в формате: "Пользователь - Оценка - Комментарий".
# # Посчитайте через цикл количество отзывов с оценкой 5 и выведите их количество в консоль.
# # Через цикл выведите только названия файлов картинок (например, "main.jpg" и "side.jpg") товара в консоль.
# # Используя цикл, найдите и выведите в консоль все отзывы пользователя с именем "techguy123".
#
#
# product1 = {
#     "productId": 1001,
#     "productName": "Wireless Headphones",
#     "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
#     "brand": "SoundPro",
#     "category": "Electronics",
#     "price": 199.99,
#     "currency": "USD",
#     "stock": {
#         "available": True,
#         "quantity": 0
#     },
#     "images": [
#         "https://example.com/products/1001/main.jpg",
#         "https://example.com/products/1001/side.jpg"
#     ],
#     "variants": [
#         {
#             "variantId": "1001_01",
#             "color": "Black",
#             "price": 199.99,
#             "stockQuantity": 20
#         },
#         {
#             "variantId": "1001_02",
#             "color": "White",
#             "price": 198.99,
#             "stockQuantity": 30
#         }
#     ],
#     "dimensions": {
#         "weight": "0.5kg",
#         "width": "18cm",
#         "height": "20cm",
#         "depth": "8cm"
#     },
#     "ratings": {
#         "averageRating": 4.7,
#         "numberOfReviews": 2
#     },
#     "reviews": [
#         {
#             "reviewId": 501,
#             "userId": 101,
#             "username": "techguy123",
#             "rating": 5,
#             "comment": "Amazing sound quality and battery life!"
#         },
#         {
#             "reviewId": 502,
#             "userId": 102,
#             "username": "jane_doe",
#             "rating": 4,
#             "comment": "Great headphones but a bit pricey."
#         }
#     ]
# }
#
#
# print(f"Количество вариантов продукта: {len(product1["variants"])}")
#
# print("\nНазвание - Цена - Количество")
# for product_variant in product1["variants"]:
#      print(f"{product_variant["variantId"]} - {product_variant["price"]} - {product_variant["stockQuantity"]}")
#
#
# sum = 0
# for product_variant in product1["variants"]:
#     if product_variant["price"] > sum:
#         sum = product_variant["price"]
#
# for product_variant in product1["variants"]:
#     if product_variant["price"] == sum:
#         print("\nВариант продукта с максимальной ценой:")
#         print(f"Название: {product_variant["variantId"]} Цена: {product_variant["price"]}")
#
#
# print("\nПользователь Оценка Комментарий")
# for review in product1["reviews"]:
#     print(f"{review["userId"]}\t\t\t\t{review["rating"]}\t{review["comment"]}")
#
#
# reviews_count = 0
# for review in product1["reviews"]:
#     if review["rating"] == 5:
#         reviews_count += 1
#
# print("\nКоличество отзывов с оценкой 5:", reviews_count)
#
# print("\nНазвания файлов картинок вариантов продуктов:")
# for image_url in product1["images"]:
#     print(image_url[image_url.rfind("/")+1:len(image_url)])
#
#
# print("\nВсе коментарии пользователя techguy123:")
# for review in product1["reviews"]:
#     if review["username"] == "techguy123":
#         for key, value in review.items():
#             print(f"{key}: {value}")