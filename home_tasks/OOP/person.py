# 6. Напишите класс Person, который имеет атрибуты name (имя), age (возраст)
# и gender (пол). Класс должен иметь следующие методы:
# • Конструктор, который принимает три параметра: name, age и gender, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Person в формате “Имя: name, Возраст: age, Пол: gender”.
# • Метод get_name, который возвращает значение атрибута name.
# • Метод set_name, который принимает один параметр: new_name, и
# устанавливает значение атрибута name равным new_name. Этот метод
# должен быть декорирован как property.
# • Метод is_adult, который возвращает True, если возраст объекта больше
# или равен 18, и False в противном случае. Этот метод должен быть
# декорирован как staticmethod.
# • Метод create_from_string, который принимает один параметр: s, и
# создает и возвращает объект класса Person на основе строки s. Строка s
# должна иметь формат “name-age-gender”, где name - имя, age - возраст и
# gender - пол. Этот метод должен быть декорирован как classmethod.

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def __str__(self):
        return f"Имя: {self.__name}, Возраст: {self.__age}, Пол: {self.__gender}"

    @property
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    # @staticmethod
    # def is_adult(person: Person) -> bool:
    #     return person.__age >= 18

    @classmethod
    def create_from_string(cls, s):
        params = s.split("-")
        person = Person(params[0], params[1], params[2])
        return person


person1 = Person("Polly", 22, "female")
print(person1)
print(person1.get_name)
person1.set_name("Polina")
print(person1.get_name)
person2 = Person.create_from_string("Filipp-16-male")
print(person2)



