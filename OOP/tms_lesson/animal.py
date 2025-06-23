class AnimalSchema:

    tail = 0

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print('Hello ' + self.name)

    def sleep(self):
        print(self.name + "is sleeping")


# Наследование
class Cat(AnimalSchema):
    tail = 1

    def speak(self):
        print('Hello, I\'m cat' + self.name)

    def sleep(self):
        print(self.name + "cat is sleeping")


class Dog(AnimalSchema):
    # Переопределение метода init
    def __init__(self, name, age, color, height, weight):
        # Вызов родительского метода через super
        super().__init__(self, name, age, color)
        self.height = height
        self.weight = weight


    def speak(self):
        print('Hello, I\'m dog' + self.name)

    def sleep(self):
        print(self.name + "dog is sleeping")

