class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            print("Ошибка формата возраста. Необходимо ввести неотрицательное целое число")
        elif 0 <= age <= 110:
            self.__age = age
        else:
            print("Недопустимые границы возраста. Введите возраст от 0 до 110")

    def print_info(self):
        print(self.__name, self.__age)


person_1 = Person("Polly", 22)
person_1.print_info()

person_1.name = "Polly2"

# обращение к сеттеру
person_1.age = "swtrbw"
person_1.age = 111
person_1.age = 23

# обращение к геттерам
print(person_1.name)
print(person_1.age)

