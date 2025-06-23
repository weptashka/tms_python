# 2) Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого необходимо создать класс
# TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от
# ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not(isinstance(self.a, int)
               and isinstance(self.b, int)
               and isinstance(self.c, int)):
            print(" – Нужно вводить только числа!")
        elif self.a < 0 or self.b < 0 or self.c < 0:
            print(" – С отрицательными числами ничего не выйдет!")
        elif (self.a + self.b >= self.c
              or self.b + self.c >= self.a
              or self.c + self.a >= self.b):
            print(" – Жаль, но из этого треугольник не сделать.")
        else:
            print(" – Ура, можно построить треугольник!")


triangle_1 = TriangleChecker(2, "wegwr", 7)
triangle_1.is_triangle()

triangle_2 = TriangleChecker(2, -5, 7)
triangle_2.is_triangle()

triangle_3 = TriangleChecker(2, 15, 7)
triangle_3.is_triangle()

triangle_4 = TriangleChecker(2, 5, 7)
triangle_4.is_triangle()

