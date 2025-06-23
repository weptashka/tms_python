class CatSchema:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def get_full_stats(self):
        return f"Color is {self.color}, Age is {self.age}, Name is {self.name}"

    # Можно в метод передавать любое слово, не только self
    def get_full_stats_2(seeeelllf):
        return f"2 Color is {seeeelllf.color}, Age is {seeeelllf.age}, Name is {seeeelllf.name}"


# Уже функция, а не метод, т.к. не внутри класса.
def get_full_stats(self):
    return f"Color is {self.color}, Age is {self.age}, Name is {self.name}"


cat_1 = CatSchema("John", "25", "blue")
# При вызове методов с "self" параметров, Python сам подставляет параметр в вызываемую функцию,
# и подставляет он сам объект (сущность), из которого вызывается.


# Вызов методов класса (объекта)
print(cat_1.get_full_stats())
print(cat_1.get_full_stats_2())

# Вызов функции и передача в неё объекта
print(get_full_stats(cat_1))


