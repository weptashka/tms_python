# --------- Home Tasks-----------
# ----- Вложенные структуры ------
from datetime import datetime, timedelta

# Задание 1

# Имеется структура данных пользователя.

# Уменьшите день рождения пользователя на 1 день.
# Измените язык пользователя на "ru".
# Измените тему на "dark".
# Измените статус активности на "false".
# Добавьте новую запись в историю активности пользователя.

user1 = {
    "userId": 2,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "profile": {
        "firstName": "Jane",
        "lastName": "Doe",
        "birthDate": "1992-04-12",
        "gender": "female",
        "avatarUrl": "https://example.com/avatars/janedoe.jpg",
        "bio": "Digital marketer and blogger."
    },
    "preferences": {
        "language": "fr",
        "theme": "light",
        "notifications": {
            "email": False,
            "sms": True,
            "push": True
        },
        "privacy": {
            "showOnlineStatus": True,
            "profileVisibility": "public"
        }
    },
    "accountStatus": {
        "isActive": True,
        "lastLogin": "2025-01-10T09:15:00Z",
        "createdAt": "2023-03-20T11:00:00Z"
    },
    "activityLogs": [
        {
            "timestamp": "2025-01-09T18:30:00Z",
            "activity": "Commented on a post"
        },
        {
            "timestamp": "2025-01-08T16:45:00Z",
            "activity": "Liked a post"
        }
    ]
}


# print("Дата рождения До: ", user1["profile"]["birthDate"])
# date_obj = datetime.strptime(user1["profile"]["birthDate"], "%Y-%m-%d")
# new_date = date_obj - timedelta(days=1)
# new_date_str = new_date.strftime("%Y-%m-%d")
# user1["profile"]["birthDate"] = new_date_str
# print("Дата рождения После: ", user1["profile"]["birthDate"])
#
# print("\nЯзык пользователя До", user1["preferences"]["language"])
# user1["preferences"]["language"] = "ru"
# print("Язык пользователя После", user1["preferences"]["language"])
#
# print("\nТема пользователя До", user1["preferences"]["theme"])
# user1["preferences"]["theme"] = "dark"
# print("Тема пользователя После", user1["preferences"]["theme"])
#
# print("\nСтатус активности пользователя До", user1["accountStatus"]["isActive"])
# user1["accountStatus"]["isActive"] = False
# print("Статус активности пользователя После", user1["accountStatus"]["isActive"])
#
# print("\nЛоги До")
# for log in user1["activityLogs"]:
#     print(f"{log["timestamp"]} : {log["activity"]}")
#
# user1["activityLogs"].append({
#     "timestamp": "2025-02-09T14:20:00Z",
#     "activity": "Forwarded post"
# })
#
# print("\nЛоги После")
# for log in user1["activityLogs"]:
#     print(f"{log["timestamp"]} : {log["activity"]}")




# Задание 2

# Имеется структура данных продукта.

# Уменьшите цену товара на 10%.
# Уменьшите количество единиц товара черного цвета на 7 (не забудьте пересчитать общее количество единиц).
# Добавьте изображение товара.
# Добавьте review для товара с рейтингом 2.
# Пересчитайте среднюю оценку товара и количество отзывов.

product1 = {
    "productId": 1001,
    "productName": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones with Bluetooth 5.0 and 20-hour battery life.",
    "brand": "SoundPro",
    "category": "Electronics",
    "price": 199.99,
    "currency": "USD",
    "stock": {
        "available": True,
        "quantity": 50
    },
    "images": [
        "https://example.com/products/1001/main.jpg",
        "https://example.com/products/1001/side.jpg"
    ],
    "variants": [
        {
            "variantId": "1001_01",
            "color": "Black",
            "price": 199.99,
            "stockQuantity": 20
        },
        {
            "variantId": "1001_02",
            "color": "White",
            "price": 199.99,
            "stockQuantity": 30
        }
    ],
    "dimensions": {
        "weight": "0.5kg",
        "width": "18cm",
        "height": "20cm",
        "depth": "8cm"
    },
    "ratings": {
        "averageRating": 4.7,
        "numberOfReviews": 2
    },
    "reviews": [
        {
            "reviewId": 501,
            "userId": 101,
            "username": "techguy123",
            "rating": 5,
            "comment": "Amazing sound quality and battery life!"
        },
        {
            "reviewId": 502,
            "userId": 102,
            "username": "jane_doe",
            "rating": 4,
            "comment": "Great headphones but a bit pricey."
        }
    ]
}


# print(product1["price"])
# product1["price"] = float(product1["price"]) * 0.9
# print(product1["price"])
#
#
# for product_variant in product1["variants"]:
#     if product_variant["color"] == "Black":
#         print(f"Количество единиц товара чёрного цвета было: {product_variant["stockQuantity"]}")
#
# for product_variant in product1["variants"]:
#     if product_variant["color"] == "Black":
#         product_variant["stockQuantity"] -= 7
#
# for product_variant in product1["variants"]:
#     if product_variant["color"] == "Black":
#         print(f"Количество единиц товара чёрного цвета стало: {product_variant["stockQuantity"]}")
#
#
# print("\nИзображения товара:")
# for image in product1["images"]:
#     print(image)
#
# product1["images"].append("https://example.com/products/1001/from_behind.jpg")
#
# print("Изображения товара после обновления:")
# for image in product1["images"]:
#     print(image)


print("\nОтзывы:")
for review in product1["reviews"]:
    print(review)

new_review = {
            "reviewId": 503,

            "userId": 666,
            "username": "holly_molly",
            "rating": 2,
            "comment": "Don't work."
        }

product1["reviews"].append(new_review)

print("\nОтзывы после обновления:")
for review in product1["reviews"]:
    print(review)

avg_rate = 0
review_count = 0
for review in product1["reviews"]:
    review_count += 1
    avg_rate += review["rating"]

avg_rate = avg_rate / review_count
print("\nСредняя оценка товаров: ", avg_rate)

print("\nКоличество отзывов: ", review_count)









