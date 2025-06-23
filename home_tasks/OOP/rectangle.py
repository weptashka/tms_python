# 5. Напишите класс Rectangle, который имеет атрибуты: width (ширина) и
# height (высота). Класс должен иметь следующие методы:
# • Конструктор, который принимает два параметра: width и height, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Rectangle в формате “Прямоугольник с шириной width и высотой
# height”.
# • Метод get_area, который возвращает площадь прямоугольника.
# • Метод get_perimeter, который возвращает периметр прямоугольника.
# • Метод is_square, который возвращает True, если прямоугольник является
# квадратом, и False в противном случае. Этот метод должен быть
# декорирован как property.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def is_square(self):
        return self.width == self.height


rect1 = Rectangle(5, 4)
print(rect1)
print(rect1.get_area())
print(rect1.get_perimeter())
print(rect1.is_square)

rect1 = Rectangle(6, 6)
print(rect1)
print(rect1.get_area())
print(rect1.get_perimeter())
print(rect1.is_square)
