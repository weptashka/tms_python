# Создать класс Matrix
#
# с конструктором
# m = Matrix([[-1, 3], [0, 1], [-2, 2]])
# но чтобы матрицы могли быть разной размерности
#
#
# методы, которые должны возвращать экземпляры класса Matrix
# - Сложение матриц (только одинаковых размерностей)
# - Вычитание матриц (точно так же).
# - Умножение матрицы на число.
# - Транспонирование матрицы
# - Возвращает новую матрицу, где вместо отрицательных чисел стоят нули
#
#
# методы, основанные на @classmethod
# - Создает единичную матрицу размером m, n
# - Создает нулевую матрицу размером m, n
# - Создает диагональную матрицу из переданного списка
#
#
# и просто методы, безо всяких условий
# - Возвращает размерность матрицы (кортеж)
# - Возвращает кол-во элементов в матрице
# - Возвращает сумму всех элементов матрицы
# - Возможность сравнения на равенство двух матриц
# - Переопределить метод __str__


class Matrix:
    def __init__(self, data):
        self.data = data

    # сложение матриц
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Можно складывать только с другим объектом Matrix.")
        if self.shape() != other.shape():
            raise ValueError("Матрицы должны быть одной размерности.")
        return Matrix([
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    # вычитание матриц
    def __sub__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Матрицы должны быть одинаковой размерности для вычитания")
        return Matrix([
            [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    # умножение матрицы на число
    def __mul__(self, scalar):
        return Matrix([[elem * scalar for elem in row] for row in self.data])

    # транспонирование
    def transpose(self):
        transposed = []
        for j in range(len(self.data[0])):
            new_row = []
            for i in range(len(self.data)):
                new_row.append(self.data[i][j])
            transposed.append(new_row)
        return Matrix(transposed)

    # возвращает матрицу, где вместо отрицательных нули
    def zero_negative(self):
        return Matrix([[elem if elem >= 0 else 0 for elem in row] for row in self.data])

    # единичная матрица
    @classmethod
    def identity(cls, m, n):
        return cls([[1 if i == j else 0 for j in range(n)] for i in range(m)])

    # нулевая матрица
    @classmethod
    def zeros(cls, m, n):
        return cls([[0 for _ in range(n)] for _ in range(m)])

    # диагональная матрица
    @classmethod
    def diagonal(cls, diag_list):
        size = len(diag_list)
        return cls([[diag_list[i] if i == j else 0 for j in range(size)] for i in range(size)])

    # размерность матрицы
    def shape(self):
        rows = len(self.data)
        cols = len(self.data[0]) if self.data else 0
        return rows, cols

    # количество элементов
    def size(self):
        return sum(len(row) for row in self.data)

    # сумма элементов
    def total(self):
        return sum(sum(row) for row in self.data)

    # сравнение матриц
    def __eq__(self, other):
        return self.data == other.data

    # переопределение __str__
    def __str__(self):
        str_matrix = ""
        for i in range(self.shape()[0]):
            for j in range(self.shape()[1]):
                str_matrix += f"{self.data[i][j]: ^{4}}"
            str_matrix += "\n"
        return str_matrix


m1 = Matrix([[-1, 1234, 5], [0, 1, 2], [-2, 2, 55]])
m2 = Matrix([[4, -3, 12], [0, 1, 2], [4, 5, -2]])
m3 = Matrix([[-1, 1234, 5], [0, 1, 2], [-2, 2, 55]])


print("m1:\n", m1.__str__())
print("m2:\n", m2.__str__())
print("m3:\n", m3.__str__())

print("Сумма m1 + m2:\n", m1 + m2)
print("Разница m1 - m2:\n", m1 - m2)
print("Умножение на число:\n", m1 * 3)
print("Транспонирование:\n", m1.transpose())
print("Отрицательные в ноль:\n", m1.zero_negative())
print("Единичная 3x3:\n", Matrix.identity(3, 3))
print("Нулевая 2x4:\n", Matrix.zeros(2, 4))
print("Диагональная:\n", Matrix.diagonal([1, 2, 3]))
print("Размерность:", m1.shape())
print("Количество элементов m1:", m1.size())
print("Сумма элементов m1:", m1.total())

print("Равны ли m1 и m3:", m1 == m3)
print("Равны ли m1 и m2:", m1 == m2)

