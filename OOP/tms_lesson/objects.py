class A:
    pass

print(A)
print(str)

a = A()

print(type(a))


class Zero:
    value = 0  # Атрибут класса


print(Zero.value)


class Cat:
    color = 'black'
    age = 1
    name = 'Tom'
    size = 'small'
    tail = 1


# Действовать напрямую с классом не очень хорошо:
print(Cat.color)
print(Cat.age)
Cat.age = 2
print(Cat.age)
# Так мы работаем с шаблоном кота


# Создание экземпляра класса - "Создание кота по шаблону"
cat_1 = Cat()
cat_2 = Cat()

# Теперь меняем свойства отдельных настоящих котов, не изменяя шаблон.
print("Шаблон: ", Cat.color)
print("Кот 1: ", cat_1.color)
print("Кот 2: ", cat_2.color)

cat_2.color = 'white'
Cat.color = 'orange'

print("Шаблон: ", Cat.color)
print("Кот 1: ", cat_1.color)
print("Кот 2: ", cat_2.color)

# У первого кота будет цвет шаблона (т.е. оранжевый), так как в объекте первого
# кота осталась ссылка на шаблон, мы не изменяли ссылку на объект, как у второго.

# Вообще не нужно менять динамические части объекта.

cat_1.color = 'white'
cat_1.color = 'orange'
Cat.color = 'white'

print("Шаблон: ", Cat.color)
print("Кот 1: ", cat_1.color)
print("Кот 2: ", cat_2.color)




#------------------ПРОСТО РАЗНОЕ------------------
class NonPositiveInt:
    def __int__(self):
        raise TypeError

class PositiveInt:
    def __init__(self, n):
        n = int(n)
        if n < 0:
            raise NonPositiveInt('Должно быть положительное число')
