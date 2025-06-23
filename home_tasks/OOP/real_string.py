# 4) Строки в Питоне сравниваются на основании значений символов. Т.е. если мы
# захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
# таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
# RealString, который будет принимать строку и сравнивать по количеству
# входящих в них символов. Сравнивать между собой можно как объекты класса,
# так и обычные строки с экземплярами класса RealString.

class RealString:
    def __init__(self, string):
        self.string = string

    def _length_of(self, other):
        if isinstance(other, RealString):
            return len(other.string)
        if isinstance(other, str):
            return len(other)
        raise TypeError("Сравнение возможно только с RealString или str")

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        return len(self) == self._length_of(other)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return len(self) < self._length_of(other)

    def __le__(self, other):
        return len(self) <= self._length_of(other)

    def __gt__(self, other):
        return len(self) > self._length_of(other)

    def __ge__(self, other):
        return len(self) >= self._length_of(other)

    def __repr__(self):
        return f"RealString('{self.string}')"


s1 = RealString("o")
s2 = RealString("Life is wonderful")
s3 = "Hey"

print(s1 > s2)
print(s1 == s2)
print(s1 < s2)

print(s2 > s3)
print(s2 == s3)
print(s2 < s3)

print(s1 > s3)
print(s1 == s3)
print(s1 < s3)




